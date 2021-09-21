#!/usr/bin/python3
"""
Flask App integrate with HTML
"""
import os
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.config["DEBUG"] = True

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
	app.run(host=os.getenv('HBNB_API_HOST') or '0.0.0.0',
	        port=os.getenv('HBNB_API_HOST') or '5000',
			threaded=True)
