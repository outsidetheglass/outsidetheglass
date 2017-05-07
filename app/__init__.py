# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# Create instance of Flask class
app = Flask(__name__)

# Config
app.config.from_object('config')

# SQL Alchemy
db = SQLAlchemy(app)

# Create Session
Session = sessionmaker()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session.configure(bind=engine)
session = Session()

from app import routes, models

if __name__ == "__main__":
    app.run()
