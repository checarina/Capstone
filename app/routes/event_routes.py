from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Event import Event
from app.models.Pet import Pet
from datetime import datetime
import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

events_bp = Blueprint("events", __name__, url_prefix = "/pets/<pet_id>/events")

#CREATE new logged event
@events_bp.route("", methods = ["POST"])
def log_event(pet_id):
    request_body = request.get_json()
    new_event = Event.from_dict(request_body, pet_id)
    db.session.add(new_event)
    db.session.commit()
    return make_response(jsonify({"event": new_event.to_dict()}), 201)

#READ all logged events for one pet
@events_bp.route("", methods = ["GET"])
def read_all_events(pet_id):
    pet = Pet.query.get(pet_id)
    pet_events = []
    for event in pet.events:
        pet_events.append(event.to_dict())
    return make_response(jsonify({f"Log for {pet.name}:": pet_events}), 200)

#READ logged events for one pet filtered by search query
#getting ambitious here
@events_bp.route("/search", methods = ["GET"])
def filter_events(pet_id, query):
    query = request.args.get("query")
    # pet = Pet.query.get(pet_id)
    query_results = Event.query.filter_by(pet_id = pet_id, type = query)
    events_result = []
    for event in query_results:
        events_result.append(event.to_dict())
    return make_response(jsonify({f"{query} events for {pet_id}:": events_result}), 200) #why is this not working


#UPDATE specific logged event
@events_bp.route("/<event_id>", methods = ["PUT"])
def update_event(pet_id, event_id):
    request_body = request.get_json()
    pet = Pet.query.get(pet_id)
    event = Event.query.get(event_id)
    event.type = request_body["type"]
    event.notes = request_body["notes"]

    db.session.commit()
    return make_response("update successful", 200)

#DELETE event

#DELETE all events (for one pet)?

