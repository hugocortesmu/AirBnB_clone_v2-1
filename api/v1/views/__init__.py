#!/usr/bin/python3
"""
creates a blueprint instances of appviews
"""
import flask

app_views = flask.Blueprint("views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *