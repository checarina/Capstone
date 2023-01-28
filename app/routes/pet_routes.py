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
@pets_bp.route("", methods = ["POST"])
def create_profile():
    request_body = request.get_json()
    # new_pet = Pet.from_dict( request_body)

    new_pet = Pet(
        name = request_body["name"],
        species = request_body["species"]
    )
    db.session.add(new_pet)
    db.session.commit()

    return make_response(jsonify({
        "pet": new_pet.name
    }), 201)

    
#READ all pet profiles

#READ one pet profile

#UPDATE pet profile

#DELETE pet profile