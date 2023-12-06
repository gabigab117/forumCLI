from database import db
from tinydb import Query, where

class Topics:
    def __init__(self, title, category, message, user):
        self.title = title
        self.category = category
        self.message = message
        self.user = user
        self.save()
    
    def save(self):
        forum = db.table("forum")
        category = forum.search(where("category") == self.category)
        category[0]["topics"].append({"title": self.title, "user": self.user, "message": [[self.message, self.user]]})
        forum.update({"topics": category[0]["topics"]}, where("category") == self.category)

# user = db.table("user").search(where("username") == "gab")