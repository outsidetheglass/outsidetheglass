# models.py

from app import app, db
from sqlalchemy import Column, Integer, String, Float

class Meteorites(db.Model):
    __tablename__ = 'meteorite_landings'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    name_type = Column(String(1000))
    rec_class = Column(String(255))
    mass = Column(String(255))
    fall = Column(String(255))
    year = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
