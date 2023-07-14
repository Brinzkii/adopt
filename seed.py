"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
harry = Pet(
    name="Harry",
    species="dog",
    photo_url="/static/boxer.jpg",
    age=2,
    notes="Very energetic and has a lazy eye",
)
bella = Pet(
    name="Bella",
    species="dog",
    photo_url="/static/pit.jpg",
    age=3,
    notes="Sassy and goes to the beat of her own drum",
)
sydney = Pet(
    name="Bella",
    species="dog",
    photo_url="/static/pit.jpg",
    age=13,
    notes="Sassy and goes to the beat of her own drum",
)

# Add new objects to session, so they'll persist
db.session.add(harry)
db.session.add(bella)


# Commit--otherwise, this never gets saved!
db.session.commit()
