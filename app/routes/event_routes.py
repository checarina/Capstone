from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Event import Event
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

events_bp = Blueprint("events", __name__, url_prefix = "/events")