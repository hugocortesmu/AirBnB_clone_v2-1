#!/usr/bin/python3
"""
Flask App integrate with HTML
"""
import os
from os import getenv
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from flask import CORS
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """
    this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

app.register_blueprint(app_views)

@app.errorhandler(404)
def erro_not_found(error):
    """status code response whit handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(host=getenv(
            'HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', 5000),
            debug=True, threaded=True)
