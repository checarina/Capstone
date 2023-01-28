from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Pet import Pet
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

pet_bp = Blueprint("pet", __name__, url_prefix = "/pet")

