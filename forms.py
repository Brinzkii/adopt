from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets to adoption database

    URL validation can be done using validators=[URL(require_tld=False, message="Please provide a valid image url")]
    however it does not like when you copy an image link from google so I removed it
    """

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField(
        "Species",
        validators=[
            AnyOf(
                values=["cat", "Cat", "dog", "Dog", "porcupine", "Porcupine"],
                message="Only cats, dogs or porcupines may be added!",
            )
        ],
    )
    photo_url = StringField("Photo (url)", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Extra details", validators=[Optional()])


class EditPetForm(FlaskForm):
    """
    Form for editing pets already in database

    URL validation can be done using validators=[URL(require_tld=False, message="Please provide a valid image url")]
    however it does not like when you copy an image link from google so I removed it
    """

    photo_url = StringField("Photo (url)", validators=[Optional()])
    notes = TextAreaField("Extra details", validators=[Optional()])
    available = BooleanField("Available")
