
## CRUD-API-FINAL


## Required Modules

- Flask
- Flask-Cors
- Flask-MySQL

## File Used

The following files are used in this project:

- `config.py`: Contains configuration settings of MySQL that will be applied in `api.py`.
- `app.py`: Implements the Flask application and API routes for `api.py`.
- `api.py`: Where the application should be. Will be run for the API to be produced.

## Description

This project is a Simple API that utilize CRUD built using Flask, Flask-Cors, and Flask-MySQL. It provides endpoints for creating, reading, updating, and deleting data in a MySQL database.

## Installation

To run this project, make sure you have Python installed. Then, follow the steps below:

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Navigate to the project directory: `cd FinalProject-IT6`
3. Create a virtual environment (optional): `python3 -m venv venv`
4. Activate the virtual environment (optional):
   - On macOS and Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate.bat`
5. Install the required modules: `pip install -r requirements.txt`
   - for required modules you can look up the pip installation
## Setting up the Database

Follow these steps to create a database and a table:

1. Open your preferred MySQL client or command-line interface.
2. Connect to your MySQL server using the appropriate credentials (host, user, root, and password if required).
3. Create a new database by executing the following query
   - CREATE DATABASE your_database_name
4. Create a new table within the database using the appropriate schema and field definitions. Here's an example:
   - CREATE TABLE your_table_name (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(50),
     email VARCHAR(100),
     age INT
     );
## Setting App and Config
1. Create `app.py` and import dependencies:
   - from flask import Flask
   - from flask_cors import CORS,cross_origin
2. Setting up the Flask application:
   - app = Flask(__name__)
   - CORS(app)
3. Create `config.py` it should contain 
   - flask-mysql module
4. Configure the MySql connection. heres and example:
   - app.config['MYSQL_DATABASE_USER'] = 'root'
   - app.config['MYSQL_DATABASE_PASSWORD'] = ''
   - app.config['MYSQL_DATABASE_DB'] = 'database'
   - app.config['MYSQL_DATABASE_HOST'] = 'localhost'
5. Modify the configuration values according to your MySQL setup. Update the following properties as required:
   - 'MYSQL_DATABASE_USER': Replace 'root' with your MySQL database username.
   - 'MYSQL_DATABASE_PASSWORD': Replace '' with your MySQL database password.
   - 'MYSQL_DATABASE_DB': Replace 'database' with the name of your MySQL database.
   - 'MYSQL_DATABASE_HOST': Replace 'localhost' with the host address of your MySQL server.
Note: Make sure you have a MySQL server running and accessible with the provided credentials.
6. Save your python files

## API logic
`api.py` is you main python program that `app.py` and `config.py` will accord to. configure your own logic and apply
CRUD method. Here is the reference for making a Flask API that utilize CRUD:
   - https://www.youtube.com/watch?v=na3MGQZdICg&t=7s
   - https://www.youtube.com/watch?v=lyosEp2tB2E

## API Endpoints
- **GET** `/api/resource`: Retrieve all resources
- **GET** `/api/resource/<id>`: Retrieve a specific resource
- **POST** `/api/resource`: Create a new resource
- **PUT** `/api/resource/<id>`: Update a specific resource
- **DELETE** `/api/resource/<id>`: Delete a specific resource

## Final Stretch
Once you configure and manage to run your code go to your API provided link and test the functionality of it. it may be
using web browsers or HHTP clients such as postman.
