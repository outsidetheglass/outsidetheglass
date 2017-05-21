# queries.py

from app import app, models, session
from sqlalchemy import func
from .models import *

def get_distinct_facilities():
    return session.query(Campsite.FacilityID, Campsite.FacilityName, Campsite.FacilityLatitude, Campsite.FacilityLongitude, Campsite.AddressStateCode, Campsite.OrgAbbrevName).distinct()

def get_facilities_by_name(facilities, name):
    return facilities.filter(Campsite.FacilityName==name)

def get_facilities_by_state(facilities, state):
    return facilities.filter(Campsite.AddressStateCode==state)

def get_facilities_by_org(facilities, org):
    return facilities.filter(Campsite.OrgAbbrevName==org)

def get_campsites(facility_id):
    return session.query(Campsite).filter(Campsite.FacilityID==facility_id).al

def create_campsite_list(facility_id):
    get_campsites(facility_id)
    campsites_list = []
    for campsite in campsites:
        campsites_list.append(campsite.CampsiteName)
    return campsites_list

def create_facility_dict(name, state, org):
    markers, facility_dict = [], {}
    facilities = get_distinct_facilities()

    if facilities != None:

        # Update query from filter form
        if name and name != "":
            facilities = get_facilities_by_name(facilities, name)
        if state and state != "":
            facilities = get_facilities_by_state(facilities, state)
        if org and org != "":
            facilities = get_facilities_by_org(facilities, org)

        # Create dictionary of attributes
        for facility in facilities:
            facility_dict['name'] = facility.FacilityName
            facility_dict['state'] = facility.AddressStateCode
            facility_dict['org'] = facility.OrgAbbrevName
            facility_dict['lat']  = facility.FacilityLatitude
            facility_dict['lng']  = facility.FacilityLongitude
            markers.append(facility_dict)
            facility_dict = {}

    return markers
