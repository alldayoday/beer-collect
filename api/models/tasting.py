from datetime import datetime
from api.models.db import db

class Tasting(db.Model):
    __tablename__ = 'tastings'
    id = db.Column(db.Integer, primary_key=True)
    shop = db.Column(db.String(250))
    impression = db.Column(db.String(250))
    date = db.Column(db.DateTime, default=datetime.now(tz=None))
    created_at = db.Column(db.DateTime, default=datetime.now(tz=None))
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'))

    def __repr__(self):
      return f"Tasting('{self.id}', '{self.impression}'"

    def serialize(self):
      return {
        "id": self.id,
        "beer_id": self.beer_id,
        "impression": self.impression,
        "shop": self.shop,
        "date": self.date.strftime('%Y-%m-%d'),
      }
