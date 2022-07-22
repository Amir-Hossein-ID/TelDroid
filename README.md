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

If you want to use redis as your database, you need `REDIS_URL` and `REDIS_PASSWORD` too. (If you are deploying on heroku, you should do this because heroku deletes the saved data after sometime.)

- Go To [Redis.com](Https://redis.com) and click "`Try Free`" in Top Right Corner to make an account.
- Choose a plan ("`Fixed Plans`" is free)
- Make a database and click "`Activate`"
- Wait until there is an url in "`Public Endpoint`" field, use it as `REDIS_URL`
- Under "Security" section, copy "`Default user password`", use it as `REDIS_PASSWORD`