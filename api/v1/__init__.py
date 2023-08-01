#!/usr/bin/python3
from flask import Blueprint

# Create a Blueprint instance with url_prefix='/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import to include all the routes defined in index.py
from api.v1.views.index import *
