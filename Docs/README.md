# Webserver API Assignment

# Problem Being Solved:

My Movie Rater webserver API is designed to Address the following problems.

## Movie Review Platform:

- Problem: Movie enthusiasts often seek reliable platforms to read and write reviews about movies. They require a space where reviews are created, posted and easily accessible/viewable.

- Solution: The developed application provides a platform that allows users to post reviews and ratings for various movies that have been stored in the database. This helps users find reviews in one place, making it easier to decide what to watch off of other users ratings and reviews.

## 2. User Authentication:

- Problem: Ensuring the credibility of reviews is highly important. un Autheticated or non genuine users can often give false or misleading information, this will ensure that does not happen as easily through making sure only authorized and verified users can post.

- Solution: The application implements user authentication, ensuring that only registered and verified users can post reviews. This adds a layer of trust and accountability to the application.

## 3. Review Management:

- Problem: The Users will need an easy way to manage their reviews which will allow them to post, view and even changed/efit their submissions.

- Solutions: The application will include ways for the user to manage their reviews easily.

# Trello Workflow Pics
### Week One
[](./Pics-files/Trello%201.png)
[](./Pics-files/TrelloCodeStructure.png)
[](./Pics-files/TrelloProjectPlanning.png)
[](./Pics-files/TrelloDocumentationQs.png)
[](./Pics-files/Trello%202.png)
[](./Pics-files/TrelloDocumentationQs1.png)
[](./Pics-files/TrelloDocumentationQs2.png)

### Week Two
[](./Pics-files/Trello%20Application%20Code1.png)
[](./Pics-files/Trello%20Application%20Code2.png)
[](./Pics-files/Trello%20Application%20Code3.png)
[](./Pics-files/Trello%20Application%20Code4.png)
[](./Pics-files/TrelloDocumentationQs3.png)
[](./Pics-files/Trello%203.png)
[](./Pics-files/TrelloDocumentationUp1.png)
[](./Pics-files/CompleteTRello.png)



# Movie Rater ERD

- [Movie Rater PDF ERD Diagram](/Docs/Pics-files/WebServerAPI.drawio.pdf)

# Packages and Dependancies 

1. Flask

- Flask is the main web framework used to build the web application. It will provide the tools to route the URLs to a specfic pyton functions, handle requests and also return responses.

2. Flask SQLAlchemy

- Flask SQLalchemy integrates with Flask allowing the application to use the database in a more Pythonic way. It will alllow or better provide ORM (object relational Mapping) making it easier to work with databases by mapping python classes to database tables.

3. Flask_bcrypt

- Brcyrpt will provide the application with the ability to hash passwords which is important in storing the password securely so outside attackers have a hard time cracking them if the database itself is hacked.

4. Flask_login

- Flask_login manages the users sessions through handling the users authentication and keeping track of the logged in user. It helps with the logging in of users aswell as logging them out and resitricting access to certain information dependant on the authenticated user.

5. Requests

- The request library will be used for making HTTP requests and routing them to the appropriate view functions.

6. JWT Token
- This will allow for the user to be given a secure token that will authorize them to use the application, this stops any melicious intent users to post reviews or rating bomb movies saved in the database through requiring the JWT token which is generated upon registering (creating) a new user.

# Features, Purpose and Function of ORM in Application

## Features: 

1. Declaritive Mapping

- SQLAlchemy will allow the developer the ability to define the models within the database using python classes. These classes will map out the database entities and their attributes within tables and columns.

2. Automated Table Creation

- Depending on the models defined SQLAlchemy will be able to automcatically create database tables.

3. Relationship Handling

- The application will support defining relationships between tables through the use of FK and PKs (foreign/Primary keys) aswell as providing utilities to handle the related Data.

4. Session Management

- SQLAlchemy provide sthe ability to manage the session so that transactions are handled correctly and also that changes in the database stick.

# Benefits and Drawbacks

## Benefits

Through using PostgreSQL the ability to do complex queries with it will make for advanced data retrieval which can be useful when ttrying to for ecxample, calculating the average rating of movies or searching/fetching user specfic reviews.

The integrity of the data will be maintained through ACID which should/will ensure all communications/transactions are handled reliably. Which is crucial for maintaining the integrity of the users information, movies, reviews and ratings.

As the movie rater database increases in size postgreSQL is properly equipped to effectievly deal with larger loads and datasets effeciently, which ensures scalability and performance of the application

Through user authentication and authorization the application will ensure secure access for users awell as allowing for roles to be set to further increase security and usablility. Having a role will allow an admin to set permissions aswell as perform actions to moderate the application (in a sense)

Through the use of the review model users will be able to provide valuable feedback about movies aswell as feedback and engagement. All this will also foster community driven content which can directly enrich and improve the user experience.

The application is built with the API First approach in mind, this will allow the application to be implemeneted in various front end clients, mobile applications or thirdparty services

## Drawbacks

Setting up the JWT and flask extensions for the application can be extensive and time consuming. Regular maintenance sush as database backups and updates also add to the complexity of the program.

Due to using postgres for handling user authentication the resource useage can be quite high and may not be suitable for limited hardware or cloud storage enviroments that are small in nature/use constrained resources.

The application in its "launch" form is very limited in what it can achieve outside of the afformentioned, reviews, rating, user storage. 

Using flaskAlchemy aswell as bcrypt and jwt creates a challenge for the developer/s to ensure all the dependancies are kept up to date and current, otherwise the application will not function properly if atall. This can be problematic for obvious reasons but maintaining the applications extensions and updates could prove long and tedious.

# How To

To use the API endpoints of this application start the application in vscode then enter the below command in the terminal.
Ensure all dependencies are installed
If using a Virtual Enviroment ensure it is enabled before running flask

```
flask run
```

This will ensure the application is connected via port.

Next open Bruno and start a new collection.
copy and paste the URI of the application that pops up when you recieve the host ip and port number from running 'flask run' and begin to create the post and get requests as follows.

1. Create User

- create post request called create user
- specify the path eg "http://127.0.0.1:5000/create_user"
- Next enter the following code snippet in json form in the body.
- testing some of the requests will require you to be an admin as they are JWT and admin only protected, meaning you will need authorization.

```json
{
  "username": "yourusername",
  "email": "youremail@hellothere.com",
  "password": "youshallnotpassword",
  "role": "admin" (optional, default is "user")
}
```
the response should look something like

```json
{
  "message": "User created successfully"
}
```
if it fails you will recieve.

```json
{
  "message": "Error message",
  "error": "Detailed error message" (only for 500 errors)
}
```
The terminal will prompt you with a more detailed error message that will help you debug what went wrong if required.

2. Login a User

- create post request called Login
- specify the path eg "http://127.0.0.1:5000/login"
- Next enter the following code snippet in json form in the body.

```json
{
  "username": "yourusername",
  "password": "youshallnotpassword"
}
```

the response if successful will be a JWT bearer token that will be useful for other requests later, so remember where it is (it may expire by the time you come back to collect it but dont worry, you can just request another via sending a post request to login again.)

```json
{
  "access_token": "JWT token"
}
```

If the request fails a 400 or 401 error message will return.

```json
{
  "message": "Error message"
}
```

More information on the errors details can be found in the terminal (or the raw data return on Bruno)


3. Add Movie (admin only)

- create post request called Add Movie
- specify the path eg "http://127.0.0.1:5000/movies"
- This will require a JWT bearers token
- go to the headers tab create a new header and type Authorization (a selector should pop up to make it quicker)
- next in the tab over write Bearer (paste JWT token here, next to it space included)
- You can copy and paste your login response token in the field next to where you made the header "Authorization". (follow the jwt bearer token paste method for all routes that require JWT)
- Next enter the following code snippet in json form in the 

```json
{
  "title": "STR",
  "description": "STR" (optional),
  "release_date": "YYYY-MM-DD" (optional),
  "rating": "float" (optional)
}
```
Response if done correctly will be

```json
{
  "message": "Movie added successfully"
}
```

If it fails this message will return, check the terminal or raw for more info.

```json
{
  "message": "Error message",
  "error": "Detailed error message" (only for 500 errors)
}
```

4. Add a Review

- create post request called add review
- specify the path eg "http://127.0.0.1:5000/(int:movie_id)/reviews"
- This will require a JWT bearers token

```json
{
  "rating": "INT",
  "review": "STR" (Not required)
}
```
The response if done correctly will be, with a (201) 

```json
{
  "message": "Review added successfully"
}
```
5. Get Movies

- create GET request called Get Movie
- specify the path eg "http://127.0.0.1:5000/movies"
- write the following snippet in the body as json entering the information of the movie desired.

```json
[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "release_date": "YYYY-MM-DD",
    "rating": "float",
    "average_rating": "float or null"
  },
]
```
6. Get Reviews for a Movie

- create GET request called Get Reviews
- specify the path eg "http://127.0.0.1:5000/movies/(enter movie_id here)/reviews"
- the following code snippet is the response from sending the GET request


A success 200: 
```json
[
  {
    "id": "INT",
    "user_id": "STR",
    "movie_id": "INT",
    "rating": "INT",
    "review": "STR",
    "timestamp": "YYYY-MM-DD HH:MM:SS"
  },
]
```
If the request fails a 404 will return

```json
{
  "message": "Error message"
}
```
Consult terminal or raw data for more information.



