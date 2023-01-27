from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    type = db.Column(db.String)
    notes = db.Column(db.String)

    pet_id = db.Column(db.Integer, db.ForeignKey("pet.id"))
    pet = db.relationship("Pet", back_populates = "events")