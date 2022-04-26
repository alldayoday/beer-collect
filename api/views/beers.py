from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.beer import Beer

beers = Blueprint('beers', 'beers')

@beers.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  beer = Beer(**data)
  db.session.add(beer)
  db.session.commit()
  return jsonify(beer.serialize()), 201