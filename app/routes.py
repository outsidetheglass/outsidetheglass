# routes.py

from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def index():
    lat, lng = None, None
    markers = [
        {
         "name": "Canada",
         "url": "https://en.wikipedia.org/wiki/Canada",
         "lat": 56.130366,
         "lng": -106.346771
        },
        {
         "name": "Anguilla",
         "url": "https://en.wikipedia.org/wiki/Anguilla",
         "lat": 18.220554,
         "lng": -63.068615
        },
        {
         "name": "Japan",
         "url": "https://en.wikipedia.org/wiki/Japan",
         "lat": 36.204824,
         "lng": 138.252924
        }
    ];
    content = {"markers": markers}

    return render_template('index.html', markers=markers)
