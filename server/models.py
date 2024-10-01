from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Create the Flask SQLAlchemy extension
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Define the Earthquake model class by inheriting from db.Model
class Earthquake(db.Model):
    __tablename__ = 'earthquakes'  # Table name for the earthquakes

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    magnitude = db.Column(db.Float, nullable=False)  # Magnitude of the earthquake
    location = db.Column(db.String, nullable=False)  # Location of the earthquake

    def __repr__(self):
        return f'<Earthquake {self.id}, Magnitude: {self.magnitude}, Location: {self.location}>'

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": self.id,
            "magnitude": self.magnitude,
            "location": self.location,
        }

# Define the Pet model class by inheriting from db.Model
class Pet(db.Model):
    __tablename__ = 'pets'  # Table name for the pets

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(50), nullable=False)  # Name of the pet
    species = db.Column(db.String(50), nullable=False)  # Species of the pet

    def __repr__(self):
        return f"<Pet {self.id}, {self.name}, {self.species}>"
