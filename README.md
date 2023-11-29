# Token-Based Authentication System API
This project is the API for the Token-Based Authentication System. It will use Python and Flask for the backend, AngularJS and Javascript for the frontend, and SQLite as the database.

## Frontend Repository

- You can find the Frontend repository at https://github.com/ejosborn/tokenbased-authsystem-frontend

## Features

- User Registration: Allow users to register by providing a unique username and password.
- User Login: Authenticate users with their username and password.
- JWT Authentication: Use JWTs to secure protected routes

## Libraries Used

- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Used to host the backend framework
- [Flask_JWT_Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) - Used for making JSON Web Tokens for only taking in valid requests
- [SQLite3](https://www.sqlite.org/index.html) - Storing user data

## Setup

### Installing
- Install Flask
```python
pip install flask
```

- Install Flask_JWT_Extended
```python
pip install flask_jwt_extended
```

- (Optional) Install dotenv
```python
pip install python-dotenv
```

- Install SQLITE3 if you have Python version 2.7.3 or older (already included if you use Python 3.X.X)
```python
pip install pysqlite
```

## Author
* **Ellis Osborn** - [Ejosborn](https://github.com/ejosborn)
