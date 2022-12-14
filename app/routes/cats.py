from flask import Blueprint, jsonify
# Hardcoded data
class Cat:
    def __init__(self, name, breed, color, size, likes_catnip):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.likes_catnip = likes_catnip

cats = [
    Cat("Garfield", "tabby", "orange", "medium", True),
    Cat("Meowy", "baby", "brown", "big", True),
    Cat("Snowball", "dilute tortie", "peach", "small", False),
]

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.route("", methods=["GET"])
def get_all_cats():
    cat_response = []
    for cat in cats:
        cat_response.append({
            "name": cat.name,
            "breed": cat.breed,
            "color": cat.color,
            "size": cat.size,
            "likes_catnip": cat.likes_catnip
        })

    return jsonify(cat_response)