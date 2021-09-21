#!/usr/bin/python3
"""
    route that returns json respone
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC
from flasgger.utils import swag_from


@app_views.route('/amenities/', methods=['GET', 'POST'])
@swag_from('swagger_yaml/amenities_no_id.yml', methods=['GET', 'POST'])
def amenities_no_id(amenity_id=None):
    """
        amenities route that handles http requests no ID given
    """
