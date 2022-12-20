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

# @cats_bp.route("/<cat_id>", methods=["GET"])
# def get_cat_by_id(cat_id):
#     cat_to_return = validate_id_and_return_cat(cat_id) 
#     return jsonify(cat_to_return.to_dict())

# def validate_id_and_return_cat(cat_id):
#     try:
#         cat_id_as_int = int(cat_id)
#     except:
#         msg = f"Cat's id {cat_id} is not an integer"
#         abort(make_response({"message": msg}, 400))

#     for cat in cats:
#         if cat.id == cat_id_as_int:
#             return cat
    
#     abort(make_response({"message": f"Cat with id {cat_id} not found"}, 404))
