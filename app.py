import os
from functools import wraps
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Initialize the application
app = Flask(__name__)

# Configuration for JWT and SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_KEY")

# Initialization of extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User Info
# Define User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')

    def __repr__(self):
        return '<User %r>' % self.username

# Admin user role route
def admin_required(fn):
    @wraps(fn)
    @jwt_required() 
    def wrapper(*args, **kwargs):
        user_identity = get_jwt_identity()
        user = User.query.filter_by(username=user_identity).first()
        if user.role != 'admin':
            return jsonify({'message': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper

# Route to create a new user
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')

    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password, role=role)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error creating user: {e}")
        return jsonify({'message': 'Error creating user', 'error': str(e)}), 500

# Route to login an existing user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        token = create_access_token(identity=username)
        return jsonify({'access_token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# Define Movie model
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    release_date = db.Column(db.Date)
    rating = db.Column(db.Float)

    def __repr__(self):
        return '<Movie %r>' % self.title

    @property
    def average_rating(self):
        reviews = Review.query.filter_by(movie_id=self.id).all()
        if not reviews:
            return None
        total_rating = sum(review.rating for review in reviews)
        return total_rating / len(reviews)

# Define Review model
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    movie = db.relationship('Movie', backref=db.backref('reviews', lazy=True))

    def __repr__(self):
        return '<Review %r>' % self.id

# Route to add a new review
@app.route('/movies/<int:movie_id>/reviews', methods=['POST'])
@jwt_required() 
def add_review(movie_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    rating = data.get('rating')
    review = data.get('review')
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if not rating:
        return jsonify({'message': 'Rating is required'}), 400

    new_review = Review(user_id=user.id, movie_id=movie_id, rating=rating, review=review)
    try:
        db.session.add(new_review)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error adding review', 'error': str(e)}), 500

    return jsonify({'message': 'Review added successfully'}), 201

# Route to get reviews for a movie
@app.route('/movies/<int:movie_id>/reviews', methods=['GET'])
def get_reviews(movie_id):
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    result = [
        {
            'id': review.id,
            'user_id': review.user_id,
            'movie_id': review.movie_id,
            'rating': review.rating,
            'review': review.review,
            'timestamp': review.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for review in reviews
    ]
    return jsonify(result), 200

# Route to get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    result = [
        {
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'release_date': movie.release_date.strftime('%Y-%m-%d') if movie.release_date else None,
            'rating': movie.rating,
            'average_rating': movie.average_rating
        } for movie in movies
    ]
    return jsonify(result), 200

# Route to add a new movie
@app.route('/movies', methods=['POST'])
@admin_required 
def add_movie():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    title = data.get('title')
    description = data.get('description')
    release_date_str = data.get('release_date')
    release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date() if release_date_str else None
    rating = data.get('rating', None)

    if not title:
        return jsonify({'message': 'Title is required'}), 400

    new_movie = Movie(title=title, description=description, release_date=release_date, rating=rating)

    try:
        db.session.add(new_movie)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error adding movie', 'error': str(e)}), 500

    return jsonify({'message': 'Movie added successfully'}), 201

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': 'An internal error occurred'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        new_user = User(username='john_doe', email='john.doe@example.com', password='password123', role='admin')
    db.session.add(new_user)
    db.session.commit()


    app.run(debug=True)