# queries.py

from app import app, models, session
from sqlalchemy import func
from .models import *

def get_distinct_facilities():
    facilities = session.query(Campsite.FacilityID, Campsite.FacilityName, Campsite.FacilityLatitude, Campsite.FacilityLongitude, Campsite.AddressStateCode).distinct()
    return facilities

def get_facilities_by_name(facilities, name):
    return facilities.filter(Campsite.FacilityName==name)

def get_facilities_by_state(facilities, state):
    return facilities.filter(Campsite.AddressStateCode==state)

def get_attributes(facility_id):
    return session.query(Campsite).filter_by(FacilityID=facility_id).first()

def create_facility_dict(name, state):
    markers, facilities_dict = [], {}
    facilities = get_distinct_facilities()

    if facilities != None:
        if name and name != "":
            facilities = get_facilities_by_name(facilities, name)
        if state and state != "":
            facilities = get_facilities_by_state(facilities, state)
        for facility in facilities:
            facilities_dict['name'] = facility.FacilityName
            facilities_dict['state'] = facility.AddressStateCode
            facilities_dict['lat']  = facility.FacilityLatitude
            facilities_dict['lng']  = facility.FacilityLongitude
            markers.append(facilities_dict)
            facilities_dict = {}
    print(markers)
    return markers
