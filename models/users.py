from database import db

from argon2 import PasswordHasher
# https://argon2-cffi.readthedocs.io/en/stable/


class User:
    def __init__(self, username, password):
        """
        Initializes a new User instance with a username and password.

        Args:
            username (str): The username of the user.
            password (str): The plaintext password of the user.
        """
        self.username = username
        self.hasher = PasswordHasher()
        self.password = self.set_password(password)
        self.save()
    
    def save(self):
        """
        Saves the user's details to the database.

        Inserts the username and hashed password into the 'user' table of the database.
        """
        db.table("user").insert({"username": self.username, "password": self.password})
    
    def set_password(self, password):
        """
        Hashes the user's password.

        Args:
            password (str): The plaintext password to hash.

        Returns:
            str: The hashed password.
        """
        return self.hasher.hash(password)