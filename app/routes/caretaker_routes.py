from app import db
from app.models.caretaker import Caretaker
from app.models.cat import Cat
from app.routes.routes_helper import validate_model
from flask import Blueprint, jsonify, make_response, request

caretakers_bp = Blueprint("caretakers_bp", __name__, url_prefix="/caretakers")

@caretakers_bp.route("", methods=["POST"])
def create_caretaker():
    caretaker_data = request.get_json()
    new_caretaker = Caretaker.from_dict(caretaker_data)

    db.session.add(new_caretaker)
    db.session.commit()

    return make_response(f"Caretaker {new_caretaker.name} created", 201)

@caretakers_bp.route("", methods=["GET"])
def get_caretakers_optional_query():
    caretaker_query = Caretaker.query

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            caretaker_query = caretaker_query.order_by(Caretaker.size.desc())
        else:
            caretaker_query = caretaker_query.order_by(Caretaker.size.asc())

    caretakers = caretaker_query.all()
    caretaker_response = []
    for caretaker in caretakers:
        caretaker_response.append(caretaker.to_dict())

    return jsonify(caretaker_response)

@caretakers_bp.route("/<caretaker_id>", methods=["GET"])
def get_caretaker_by_id(caretaker_id):
    caretaker_to_return = validate_model(Caretaker, caretaker_id)

    return jsonify(caretaker_to_return.to_dict())

@caretakers_bp.route("/<caretaker_id>/cats", methods=["POST"])
def add_new_cat_to_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()

    new_cats = []
    cat_names = []
    for cat in request_body:
        new_cat = Cat.from_dict(cat)
        new_cat.caretaker = caretaker

        new_cats.append(new_cat)
        cat_names.append(cat["name"])

    db.session.add_all(new_cats)
    db.session.commit()

    message = f"Cat(s) {','.join(cat_names)} created with Caretaker {caretaker.name}"
    return make_response(jsonify(message), 201)

@caretakers_bp.route("/<caretaker_id>/cats", methods=["GET"])
def get_all_cats_for_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)

    cats_response = []
    for cat in caretaker.cats:
        cats_response.append(cat.to_dict())

    return jsonify(cats_response)