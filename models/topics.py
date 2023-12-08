from database import db
from tinydb import Query, where

class Topics:
    def __init__(self, title, category, message, username):
        self.title = title
        self.category = category
        self.message = message
        self.username = username
        self.save()
    
    def save(self):
        forum = db.table("forum")
        category = forum.search(where("category") == self.category)
        category[0]["topics"].append({"title": self.title, "user": self.username, "message": [[self.message, self.username]]})
        forum.update({"topics": category[0]["topics"]}, where("category") == self.category)