# routes.py

from flask import render_template, redirect, url_for
from app import app
from .models import *
from .queries import *
from .forms import *

@app.route('/')
def index():
    form = StateForm()
    query = get_all_campsites()
    content = {"form": form}
    return render_template('index.html', content=content)
