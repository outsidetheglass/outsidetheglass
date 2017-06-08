# __init__.py

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy


# Create instance of Flask class
app = Flask(__name__)

# Config
app.config.from_object('config')

# SQL Alachemy
db = SQLAlchemy()

# Create Session
Session = sessionmaker()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session.configure(bind=engine)
session = Session()

from app import routes, models
