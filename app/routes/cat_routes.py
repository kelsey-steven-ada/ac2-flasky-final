from app import db
from app.models.cat import Cat
from flask import Blueprint, jsonify, abort, make_response, request

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.route("", methods=["POST"])
def create_cat():
    cat_data = request.get_json()

    new_cat = Cat(
        name = cat_data["name"],
        breed = cat_data["breed"],
        color = cat_data["color"],
        size = cat_data["size"],
        likes_catnip = cat_data["likes_catnip"]
    )

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} created", 201)

@cats_bp.route("", methods=["GET"])
def get_all_cats():
    all_cats = Cat.query.all()
    cat_response = []
    for cat in all_cats:
        cat_response.append({
            "id": cat.id,
            "name": cat.name,
            "breed": cat.breed,
            "color": cat.color,
            "size": cat.size,
            "likes_catnip": cat.likes_catnip,
        })

    return jsonify(cat_response)

@cats_bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    cat_to_return = validate_id_and_return_cat(cat_id)

    return jsonify({
        "id": cat_to_return.id,
        "name": cat_to_return.name,
        "breed": cat_to_return.breed,
        "color": cat_to_return.color,
        "size": cat_to_return.size,
        "likes_catnip": cat_to_return.likes_catnip,
    })

@cats_bp.route("/<cat_id>", methods=["PUT"])
def replace_cat_with_id(cat_id):
    cat_data = request.get_json()
    cat_to_update = validate_id_and_return_cat(cat_id)

    cat_to_update.name = cat_data["name"],
    cat_to_update.breed = cat_data["breed"],
    cat_to_update.color = cat_data["color"],
    cat_to_update.size = cat_data["size"],
    cat_to_update.likes_catnip = cat_data["likes_catnip"]

    db.session.commit()

    return make_response(f"Cat {cat_to_update.name} updated", 200)

@cats_bp.route("/<cat_id>", methods=["DELETE"])
def delete_cat_by_id(cat_id):
    cat_to_delete = validate_id_and_return_cat(cat_id)
    db.session.delete(cat_to_delete)
    db.session.commit()

    return make_response(f"Cat {cat_to_delete.name} deleted", 200)

def validate_id_and_return_cat(cat_id):
    try:
        cat_id_as_int = int(cat_id)
    except:
        msg = f"Cat's id {cat_id} is not an integer"
        abort(make_response({"message": msg}, 400))

    cat = Cat.query.get(cat_id_as_int)
    if cat:
        return cat
    
    abort(make_response({"message": f"Cat with id {cat_id} not found"}, 404))
