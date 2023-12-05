from database import db

class Category:
    def __init__(self, name):
        self.name = name
        self.save()
    
    def save(self):
        db.table("forum").insert({"category": self.name, "topics": []})