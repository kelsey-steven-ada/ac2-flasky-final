from app import db

class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    cats = db.relationship("Cat", back_populates="caretaker")

    def to_dict(self):
        caretaker_dict = {}
        caretaker_dict["id"] = self.id
        caretaker_dict["name"] = self.name

        cat_names = []
        for cat in self.cats:
            cat_names.append(cat.name)
        caretaker_dict["cats"] = cat_names

        return caretaker_dict

    @classmethod
    def from_dict(cls, caretaker_data):
        new_caretaker = Caretaker(
            name = caretaker_data["name"]
        )
        return new_caretaker