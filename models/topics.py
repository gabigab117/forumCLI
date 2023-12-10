from database import db
from tinydb import Query, where

class Topics:
    def __init__(self, title, category, message, username):
        """
        Initialize a new topic with the given title, category, message, and username.
        Upon initialization, it also saves the topic to the database.

        Args:
        title (str): The title of the topic.
        category (str): The category under which the topic falls.
        message (str): The initial message or content of the topic.
        username (str): The username of the person who created the topic.
        """
        self.title = title
        self.category = category
        self.message = message
        self.username = username
        self.save()
    
    def save(self):
        """
        Saves the current topic to the database. It searches for the specified category in the database,
        appends the new topic to this category, and updates the database with the new topic list.
        """
        forum = db.table("forum")
        category = forum.search(where("category") == self.category)
        category[0]["topics"].append({"title": self.title, "user": self.username, "message": [[self.message, self.username]]})
        forum.update({"topics": category[0]["topics"]}, where("category") == self.category)