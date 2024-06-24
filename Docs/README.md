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

The benefits of this application is through the use of blueprints/models making the project larger will be easier, aswell as being easier to scale. The project will remain easy to manage due to the sepration of specific parts of the application aswell

Security through the use of hashing passwords using bcrypt will allow the application to enhance the security of sensitive user information. Using JWT tokens will add another layer of secrutiy through requiring the user to authenticate/Authorize a token to access the information on the database specific to them.

Through the use of flask-login, users sessions will be stored for the user logged in which will improve the management system and experience
