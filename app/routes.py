# routes.py

from flask import render_template, redirect, url_for
from app import app
from .models import *
from .queries import *

@app.route('/')
def index():
    query = get_all_campsites()
    content = {}

    return render_template('index.html', content=content)
