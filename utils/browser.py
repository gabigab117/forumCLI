from tinydb import where
from argon2 import PasswordHasher
from database import db


class AuthError(Exception):
    pass

class Browser:
    def __init__(self, username, password):
        self.hasher = PasswordHasher()
        self.users = db.table("user")
        self.username = username
        self.auth = self.authenticate(password)
    
    def authenticate(self, password):
        user = self.users.search(where("username") == self.username)
        if user:
            return self.hasher.verify(user[0]["password"], password)
        else:
            raise AuthError("No account for this username")

