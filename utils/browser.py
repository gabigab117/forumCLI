from tinydb import where
from argon2 import PasswordHasher
from database import db
from rich.table import Table
from rich.console import Console


class AuthError(Exception):
    pass

class Browser:
    def __init__(self, username):
        self.hasher = PasswordHasher()
        self.users = db.table("user")
        self.username = username
        self.auth = False
    
    def authenticate(self, password):
        user = self.users.search(where("username") == self.username)
        if user:
            self.auth = self.hasher.verify(user[0]["password"], password)
            return self.auth
        else:
            raise AuthError("No account for this username")
    
    def display_category(self):
        forum = db.table("forum")
        table = Table(title="Catégories")
        table.add_column("Catégories")
        for category in forum:
            table.add_row(category["category"])
        
        console = Console()
        console.print(table)
