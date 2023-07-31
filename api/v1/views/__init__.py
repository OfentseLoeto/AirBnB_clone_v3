#!/usr/bin/python3
"""create a variable app_views which is an instance
   of Blueprint (url prefix must be /api/v1)
"""
from flask import Blueprint

"""A blueprint instance with url_prefix='/api/v1'"""

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
