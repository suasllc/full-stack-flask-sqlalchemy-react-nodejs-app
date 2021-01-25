from .db import db

class Location(db.Model):
    __tablename__ = 'locations'


    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)

    # to_dict method to convert a dataframe into a dictionary of series or list like data type depending on orient parameter
    def to_dict(self):
        return {
        "id": self.id,
        "city": self.city,
        "state": self.state,
        "country": self.country
        }