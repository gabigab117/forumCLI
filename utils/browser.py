from tinydb import where
from argon2 import PasswordHasher
from database import db
from rich.table import Table
from rich.console import Console
from security import AuthError, is_authenticate

class Browser:
    def __init__(self, username):
        self.hasher = PasswordHasher()
        self.users = db.table("user")
        self.username = username
        self.auth = False
        self.console = Console()
    
    def authenticate(self, password):
        user = self.users.search(where("username") == self.username)
        if user:
            self.auth = self.hasher.verify(user[0]["password"], password)
            return self.auth
        else:
            raise AuthError("No account for this username")
    
    def display_categories(self):
        is_authenticate(self.auth)
        forum = db.table("forum")
        table = Table(title="Catégories")
        table.add_column("Catégories")
        [table.add_row(category["category"]) for category in forum]
        
        self.console.print(table)
    
    def display_topics(self, category_name):
        is_authenticate(self.auth)
        forum = db.table("forum")
        table = Table(title=f"Sujets de la catégorie {category_name}")
        table.add_column("Sujets")
        table.add_column("Auteurs")
        category = forum.search(where("category") == category_name)
        [table.add_row(el["title"], el["user"]) for el in category[0]["topics"]]

        self.console.print(table)
    
    def display_messages(self, category_name, topic_title):
        is_authenticate(self.auth)
        forum = db.table("forum")
        table = Table(title=f"Messages du sujet {topic_title}")
        table.add_column("Messages")
        table.add_column("Auteurs")
        category = forum.search(where("category") == category_name)
        for el in category[0]["topics"]:
            [table.add_row(message_list[0], message_list[1]) for message_list in el["message"] if el["title"] == topic_title]
        
        self.console.print(table)

    
    def add_message(self, category_name, topic_title, message):
        is_authenticate(self.auth)
        forum = db.table("forum")
        category = forum.search(where("category") == category_name)
        [el["message"].append([message, self.username]) for el in category[0]["topics"] if el["title"] == topic_title]
        forum.update({"topics": category[0]["topics"]}, where("category") == category_name)
