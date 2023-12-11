import pytest
import os
from tinydb import TinyDB

@pytest.fixture(scope="class")
def db_management():
    db_path = "tests/db_test.json"
    db = TinyDB(db_path)
    yield db
    os.remove(db_path)
