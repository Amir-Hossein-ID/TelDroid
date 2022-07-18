# TelDroid
Telegram Userbot, Written in Python Using [Telethon](https://github.com/LonamiWebs/Telethon).

<br/>

# How To Deploy
- [Heroku](#deploy-to-heroku)
- [Locally](#deploy-locally)

## Deploy to Heroku
Prepare the [Required Variables](#required-variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploy Locally
- Clone the repository
- Install requirements by running `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
- Edit the `.env` file and set the [Required Variables](#required-variables) like this:
    ```
    API_ID=11111
    API_HASH=aaaaaaaaaaaaaaaaaaa
    SESSION_STRING=asdjaskd86qq3eh3qjke3g3ke3h
    ```
- Run the bot by running `python teldroid.py` or `python3 teldroid.py`

# Required Variables
- `API_ID` - Get it from [my.telegram.org](https://my.telegram.org/) or [@ScrapperRoBot](https://t.me/ScrapperRoBot)
- `API_HASH` - Get it from [my.telegram.org](https://my.telegram.org/) or [@ScrapperRoBot](https://t.me/ScrapperRoBot)
- `SESSION_STRING` - Get it from [@SessionStringBot](https://t.me/SessionStringBot) or by running `python session_gen.py` or `python3 session_gen.py`
