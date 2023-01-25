from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    breed = db.Column(db.String)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    pic = db.Column(db.String) #image URL
    details = db.Column(db.String)

    events = db.relationship("Event", back_populates = "pet")