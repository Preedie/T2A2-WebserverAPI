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

