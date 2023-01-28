from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Pet import Pet
from datetime import datetime
import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

pets_bp = Blueprint("pets", __name__, url_prefix = "/pets")

#CREATE new pet profile

#READ all pet profiles

#READ one pet profile

#UPDATE pet profile

#DELETE pet profile