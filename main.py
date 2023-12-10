import typer

from rich.progress import track
import time

from utils import Browser
from models import Topics


app = typer.Typer()

s = Browser("")

def signin(s):
    s.authenticate()


@app.command()
def signup(username: str):
    s = Browser(username)
    s.signup()
    total = 0
    for value in track(range(100), description="Inscription en cours"):
        time.sleep(0.01)
        total += 1
    print(f"Inscription de {username} en terminée.")


@app.command()
def display_categories():
    total = 0
    for _ in track(range(100), description="Affichage des catégories en cours"):
        time.sleep(0.01)
        total += 1
    print(f"Liste des catégories")

    s.display_categories()


@app.command()
def display_topics(category: str):
    total = 0
    for _ in track(range(100), description="Affichage des sujets en cours"):
        time.sleep(0.01)
        total += 1
    print(f"Liste des sujets.")

    s.display_topics(category)


@app.command()
def new_topic(username, title, category, message):
    s = Browser(username)
    signin(s)
    Topics(title, category, message, username)
    total = 0
    for _ in track(range(100), description="Publication en cours"):
        time.sleep(0.01)
        total += 1
    print(f"Liste des sujets.")
    s.display_messages(category, title)


@app.command()
def add_message(username: str, category_name: str, topic_title: str, message: str):
    s = Browser(username)
    signin(s)
    s.add_message(category_name, topic_title, message)
    s.display_messages(category_name, topic_title)



app()