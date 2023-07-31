#!/usr/bin/python3
"""Create a route /status on the object app_views
   that returns a JSON status OK.
"""
from api.v1.views import app_views
from flask import jsonify

"""Routesthe status of an API"""
@app_views.route('/status', methods=['GET'])

def get_status():
    return jsonify(status'OK')
