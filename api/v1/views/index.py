#!/usr/bin/python3
"""
Flask route returns json status
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage