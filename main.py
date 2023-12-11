import typer

from utils import Browser
from models import Topics
from for_fun import progress_bar


app = typer.Typer()

s = Browser("")

def signin(s):
    s.authenticate()


@app.command()
def signup(username: str):
    s = Browser(username)
    s.signup()
    progress_bar("Inscription en cours")
    print(f"Inscription de {username} en terminée.")


@app.command()
def display_categories():
    progress_bar("Affichage des catégories en cours")
    print(f"Liste des catégories")

    s.display_categories()


@app.command()
def display_topics(category: str):
    progress_bar("Affichage des sujets en cours")
    print(f"Liste des sujets.")

    s.display_topics(category)


@app.command()
def new_topic(username: str, category: str, title: str, message: str):
    s = Browser(username)
    signin(s)
    Topics(title, category, message, username)
    progress_bar("Publication en cours")
    print(f"Liste des sujets.")
    s.display_messages(category, title)


@app.command()
def add_message(username: str, category_name: str, topic_title: str, message: str):
    s = Browser(username)
    signin(s)
    progress_bar("Publication du message...")
    s.add_message(category_name, topic_title, message)
    s.display_messages(category_name, topic_title)



app()