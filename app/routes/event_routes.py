from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Event import Event
from app.models.Pet import Pet
from datetime import datetime
import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

events_bp = Blueprint("events", __name__, url_prefix = "/<pet_id>/events")

#CREATE new logged event
@events_bp.route("", methods = ["CREATE"])
def log_event(pet_id):
    request_body = request.get_json()
    new_event = Event.from_dict(request_body)
    db.session.add(new_event)
    db.session.commit()
    return make_response(jsonify({"event": new_event.to_dict()}), 201)

#READ all logged events for one pet

#READ logged events for one pet filtered by search query
#getting ambitious here

#UPDATE specific logged event

#DELETE event

#DELETE all events (for one pet)?

