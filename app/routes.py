# routes.py

from flask import render_template, redirect, request, url_for
from react.render import render_component
import os
from app import app
from .models import *
from .queries import *
from .forms import *

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StateForm(request.form, csrf_enabled=True)
    name, state, org = form.name.data, form.state.data, form.org.data

    rendered = render_component(
          os.path.join(os.getcwd(), 'static', 'js', 'CommentBox.jsx'),
          {
              'comments': comments,
              'url': '/comment/',
          },
          to_static_markup=True,
    )

    # --- POST ---
    if request.method == 'POST':
        query = create_facility_dict(name, state, org)
        print(query)

    # --- GET ---
    content = {"form": form, "rendered": rendered}
    return render_template('index.html', content=content)
