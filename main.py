import typer

from utils import Browser
from models import Topics, Category
from for_fun import progress_bar


app = typer.Typer()

s = Browser("")

def signin(s):
    s.authenticate()


@app.command()
def signup(username: str):
    """
    Sign up a new user with the provided username.
    """
    s = Browser(username)
    s.signup()
    progress_bar("Inscription en cours")
    print(f"Inscription de {username} en terminée.")


@app.command()
def display_categories():
    """
    Display a list of categories.
    """
    progress_bar("Affichage des catégories en cours")
    print(f"Liste des catégories")

    s.display_categories()


@app.command()
def display_topics(category: str):
    """
    Display topics within a specified category.
    """
    progress_bar("Affichage des sujets en cours")
    print(f"Liste des sujets.")

    s.display_topics(category)


@app.command()
def new_category(username: str, name: str):
    """
    Create and display a new topic in a specified category by a user.
    """
    s = Browser(username)
    signin(s)
    Category(name)
    progress_bar("Publication en cours")
    print(f"Liste des catégories.")
    s.display_categories()


@app.command()
def new_topic(username: str, category: str, title: str, message: str):
    """
    Create and display a new topic in a specified category by a user.
    """
    s = Browser(username)
    signin(s)
    Topics(title, category, message, username)
    progress_bar("Publication en cours")
    print(f"Liste des sujets.")
    s.display_messages(category, title)


@app.command()
def add_message(username: str, category_name: str, topic_title: str, message: str):
    """
    Add a message to a specific topic and display updated messages.
    """
    s = Browser(username)
    signin(s)
    progress_bar("Publication du message...")
    s.add_message(category_name, topic_title, message)
    s.display_messages(category_name, topic_title)



app()