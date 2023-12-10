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

[![Demo Video for Forum CLI project](https://www.gabrieltrouve.fr/media/images/youtube_social_icon_white.original.png)](https://youtu.be/YElyXuaEU9Q?si=mEbmjtnpmAfolRtJ)