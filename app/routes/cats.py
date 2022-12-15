from flask import Blueprint, jsonify, abort, make_response
# Hardcoded data
class Cat:
    def __init__(self, id, name, breed, color, size, likes_catnip):
        self.id = id
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.likes_catnip = likes_catnip

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "color": self.color,
            "size": self.size,
            "likes_catnip": self.likes_catnip
        }

cats = [
    Cat(1, "Garfield", "tabby", "orange", "medium", True),
    Cat(2, "Meowy", "baby", "brown", "big", True),
    Cat(3, "Snowball", "dilute tortie", "peach", "small", False),
]

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.route("", methods=["GET"])
def get_all_cats():
    cat_response = []
    for cat in cats:
        cat_response.append(cat.to_dict())

    return jsonify(cat_response)

def validate_id_and_return_cat(cat_id):
    try:
        cat_id_as_int = int(cat_id)
    except:
        msg = f"Cat's id {cat_id} is not an integer"
        abort(make_response({"message": msg}, 400))

    for cat in cats:
        if cat.id == cat_id_as_int:
            return cat
    
    abort(make_response({"message": f"Cat with id {cat_id} not found"}, 404))

@cats_bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    cat_to_return = validate_id_and_return_cat(cat_id) 
    return jsonify(cat_to_return.to_dict())

