from flask import render_template, flash, redirect
from app import app


@app.route('/')
def index():
    content = {}
    return render_template('index.html', content)
