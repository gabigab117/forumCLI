from models import User, Category
from tinydb import where
from argon2 import PasswordHasher

class TestModels:

    @classmethod
    def setup_class(cls):
        cls.user = User("gab", "test")
        cls.category = Category("Première")
        
    def test_user_is_init(self, db_management):
        # Given : An user
        # When : is registered in BDD
        user = db_management.table("user").search(where("username") == "gab")[0]["username"]
        # Then : the request return de username
        assert self.user.username == user

    def test_password_is_hash(self):
        # Given : An user
        # When : is registered in BDD
        # Then : the password is hashed
        assert self.user.password != "test"
    
    def test_category_in_bdd(self, db_management):
        # Given : a category
        # When : is registered in BDD
        category = db_management.table("forum").search(where("category") == "Première")
        # Then : the request return category name
        assert self.category.name == category[0]["category"]
    
    def test_auth_is_success(self, db_management):
        ph = PasswordHasher()
        assert ph.verify(db_management.table("user").search(where("username") == "gab")[0]["password"], "test") is True