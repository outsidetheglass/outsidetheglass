from app import app, models, session
from sqlalchemy import func
from .models import *

def get_url(facility_id, facility_name):
    facility = format_name(facility_name)
    park_id = facility_id
    return "https://www.recreation.gov/camping/{0}/r/campgroundDetails.do?contractCode=NRSO&parkId={1}".format(facility, park_id)

def format_name(facility_name):
    modified = ""
    for char in facility_name:
        if char == " ":
            char = "-"
        modified += char
    return modified
