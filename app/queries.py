# queries.py

from app import app, models, session
from sqlalchemy import func
from .models import *

def get_meteorites():
    landings = session.query(Meteorites).filter(Meteorites.latitude!=0, Meteorites.latitude!=None, Meteorites.longitude!=0, Meteorites.longitude!=None).all()
    return landings

def get_meteorites_by_year(year):
    landings = session.query(Meteorites).filter_by(year=year).filter(Meteorites.latitude!=0, Meteorites.latitude!=None, Meteorites.longitude!=0, Meteorites.longitude!=None).all()
    return landings

def create_meteorite_dict(year):
    m, d = [], {}

    # if year:
    #     meteorites = get_meteorites_by_year(year)
    # else:
    meteorites = get_meteorites()

    for meteorite in meteorites:
        d["name"] = meteorite.name
        d["mass"] = meteorite.mass
        d["rec_class"] = meteorite.rec_class
        d["year"] = meteorite.year
        d["lat"] = meteorite.latitude
        d["long"] = meteorite.longitude
        m.append(d)
        d = {}
    return m
