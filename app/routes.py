# routes.py

from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def index():
    lat, lng = None, None
    coord = {'lat': lat, "lng": lng}
    api_code = "https://maps.googleapis.com/maps/api/js?key={}&callback=initMap".format(app.config['GOOGLE_MAPS_API_CODE'])
    content = {"api_code": api_code}

    return render_template('index.html', content=content)
