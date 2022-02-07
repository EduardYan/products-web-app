"""
This is the file, for some configurations
and hooks for the server. For execute the server
execute the file index.py
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.products import products
from config import CONFIG

# creating the server
server = Flask(__name__)

# settings
server.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLITE_CONNECTION']
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.secret_key = 'mysecretkey'

# database initilization
SQLAlchemy(server)

# using routes
server.register_blueprint(products)
