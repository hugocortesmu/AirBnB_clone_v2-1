#!/usr/bin/python3

import os 
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from flask_cors import CORS
app = Flask(__name__)
