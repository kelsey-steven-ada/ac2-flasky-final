from app import db
from app.models.cat import Cat
from app.routes.routes_helper import validate_model
from flask import Blueprint, jsonify, make_response, request

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.route("", methods=["POST"])
def create_cat():
    cat_data = request.get_json()
    new_cat = Cat.from_dict(cat_data)

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} created", 201)

@cats_bp.route("", methods=["GET"])
def get_cats_optional_query():
    cat_query = Cat.query

    breed_query = request.args.get("breed")
    if breed_query:
        # Case sensitive, exact match
        # cat_query = cat_query.filter_by(breed=breed_query)

        # Case sensitive, partial match
        # cat_query = cat_query.filter(Cat.breed.contains(breed_query))

        # Case insensitive, partial match
        cat_query = cat_query.filter(Cat.breed.ilike(f"%{breed_query}%"))

    catnip_query = request.args.get("likes_catnip")
    if catnip_query:
        cat_query = cat_query.filter_by(likes_catnip=catnip_query)

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            cat_query = cat_query.order_by(Cat.size.desc())
        else:
            cat_query = cat_query.order_by(Cat.size.asc())

    cats = cat_query.all()
    cat_response = []
    for cat in cats:
        cat_response.append(cat.to_dict())

    return jsonify(cat_response)

@cats_bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    cat_to_return = validate_model(Cat, cat_id)

    return jsonify(cat_to_return.to_dict())

@cats_bp.route("/<cat_id>", methods=["PUT"])
def replace_cat_with_id(cat_id):
    cat_data = request.get_json()
    cat_to_update = validate_model(Cat, cat_id)

    cat_to_update.name = cat_data["name"],
    cat_to_update.breed = cat_data["breed"],
    cat_to_update.color = cat_data["color"],
    cat_to_update.size = cat_data["size"],
    cat_to_update.likes_catnip = cat_data["likes_catnip"]

    db.session.commit()

    return make_response(f"Cat {cat_to_update.name} updated", 200)

@cats_bp.route("/<cat_id>", methods=["DELETE"])
def delete_cat_by_id(cat_id):
    cat_to_delete = validate_model(Cat, cat_id)
    db.session.delete(cat_to_delete)
    db.session.commit()

    return make_response(f"Cat {cat_to_delete.name} deleted", 200)