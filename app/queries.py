# queries.py

from app import app, models, session
from sqlalchemy import func
from .models import *

def get_all_campsites():
    markers, campsite_dict = [], {}
    campsites = session.query(Campsite.FacilityName, Campsite.FacilityLatitude, Campsite.FacilityLongitude).distinct()
    if campsites != None:
        for campsite in campsites:
            campsite_dict['name'] = campsite.FacilityName
            campsite_dict['lat']  = campsite.FacilityLatitude
            campsite_dict['lng']  = campsite.FacilityLongitude
            markers.append(campsite_dict)
            campsite_dict = {}
    return markers

def get_city_sites():
    pass
