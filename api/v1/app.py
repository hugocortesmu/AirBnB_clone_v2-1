#!/usr/bin/python3
"""
Flask App integrate with HTML
"""
from os import getenv
import os
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
<<<<<<< HEAD

=======
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
>>>>>>> bb4102fb478b4e661c515a33e22aa1e4355239a6
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

<<<<<<< HEAD

if __name__ == "__main__":
    app.run(host=getenv(
            'HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', 5000),
            debug=True, threaded=True)
=======
@app.errorhandler(404)
def erro_not_found(error):
    """status code response whit handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)
>>>>>>> bb4102fb478b4e661c515a33e22aa1e4355239a6
