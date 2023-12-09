import typer

from utils import Browser


app = typer.Typer()

s = Browser("")

def signin(s):
    s.authenticate()


@app.command()
def signup(username: str):
    s = Browser(username)
    s.signup()


@app.command()
def display_categories():
    s.display_categories()


@app.command()
def display_topics():
    s.display_topics()


@app.command()
def add_message(username: str, category_name: str, topic_title: str, message: str):
    s = Browser(username)
    signin(s)
    s.add_message(category_name, topic_title, message)



app()