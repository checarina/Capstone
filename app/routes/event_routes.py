from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Event import Event
from app.models.Pet import Pet
from datetime import datetime
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

events_bp = Blueprint("events", __name__, url_prefix = "pets/<pet_id>/events")

#CREATE new logged event

#READ all logged events for one pet

#READ logged events for one pet filtered by search query
#getting ambitious here

#UPDATE specific logged event

#DELETE event

#DELETE all events (for one pet)?

