from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_bcrypt import Bcrypt
from datetime import datetime

# initialize application
app = Flask(__name__)

# config for JWT and Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'http://localhost:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = ''

# Initialization of extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Route to login an existing user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': username, 'email': user.email})
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# User Info
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Route to create a new user
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})

# Define Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    release_date = db.Column(db.Date)
    rating = db.Column(db.Float)

#Defining movie review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('reviews'))
    movie = db.relationship('Movie', backref=db.backref('reviews'))

# Route to add a new review
@app.route('/movies/<int:movie_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(movie_id):
    data = request.get_json()
    rating = data.get('rating')
    review = data.get('review')
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    new_review = Review(user_id=user.id, movie_id=movie_id, rating=rating, review=review)
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify({'message': 'Review added successfully'}), 201

# Route to get reviews for a movie
@app.route('/movies/<int:movie_id>/reviews', methods=['GET'])
def get_reviews(movie_id):
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    result = []
    for review in reviews:
        result.append({
            'id': review.id,
            'user_id': review.user_id,
            'movie_id': review.movie_id,
            'rating': review.rating,
            'review': review.review,
            'timestamp': review.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result)

# Route to get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    result = []
    for movie in movies:
        result.append({
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'release_date': movie.release_date.strftime('%Y-%m-%d') if movie.release_date else None,
            'rating': movie.rating
        })
    return jsonify(result)

# Route to add a new movie
@app.route('/movies', methods=['POST'])
@jwt_required()
def add_movie():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    release_date_str = data.get('release_date')
    release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date() if release_date_str else None
    rating = data.get('rating')

    new_movie = Movie(title=title, description=description, release_date=release_date, rating=rating)
    db.session.add(new_movie)
    db.session.commit()
    
    return jsonify({'message': 'Movie added successfully'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)