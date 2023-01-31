from app import db

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    likes_catnip = db.Column(db.Boolean, nullable=False, default=True)
    pet_count = db.Column(db.Integer, nullable=False, default=0)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))
    caretaker = db.relationship("Caretaker", back_populates="cats")

    def to_dict(self):
        cat_dict = {}
        cat_dict["id"] = self.id
        cat_dict["name"] = self.name
        cat_dict["breed"] = self.breed
        cat_dict["color"] = self.color
        cat_dict["size"] = self.size
        cat_dict["likes_catnip"] = self.likes_catnip
        cat_dict["pet_count"] = self.pet_count

        if self.caretaker:
            cat_dict["caretaker"] = self.caretaker.name

        return cat_dict

    @classmethod
    def from_dict(cls, cat_data):
        new_cat = Cat(
            name = cat_data["name"],
            breed = cat_data["breed"],
            color = cat_data["color"],
            size = cat_data["size"]
        )

        if "likes_catnip" in cat_data:
            new_cat.likes_catnip = cat_data["likes_catnip"]

        if "pet_count" in cat_data:
            new_cat.pet_count = cat_data["pet_count"]

        return new_cat