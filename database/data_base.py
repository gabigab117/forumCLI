from tinydb import TinyDB
import sys


TEST_MODE = "pytest" in sys.modules

db = TinyDB("db.json") if not TEST_MODE else TinyDB(r"tests/db_test.json")
