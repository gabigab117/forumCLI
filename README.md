# Forum CLI (Décembre 2023)

With this project, I want to create a CLI forum with the creation of user accounts, creation of categories, possibility of posting messages.


## Security

I use Argon2 so as not to store passwords in clear text.

## Database

I found TinyDB to be perfectly suited for this type of project.

## CLI ?

I use Typer, so from the terminal you can generate the documentation and available commands.

Example, display project documentation : 

```
python main.py --help
```

## Demo

https://youtu.be/6pfKjq7C2mU