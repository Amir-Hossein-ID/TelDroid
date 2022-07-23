import os

from telethon import TelegramClient
from telethon.sessions import StringSession

import plugins
import shared


def start_db():
    if os.getenv("REDIS_URL", "") and os.getenv("REDIS_PASSWORD", ""):
        shared.db = shared.RedisDB(os.getenv("REDIS_URL"), os.getenv("REDIS_PASSWORD"))
    else:
        shared.db = shared.SQLiteDB("data.db")

def start_bot():
    start_db()
    userbot = TelegramClient(StringSession(os.getenv('SESSION_STRING')), os.getenv('API_ID'), os.getenv('API_HASH'))
    userbot.start()
    plugin_manager = plugins.PluginManager()

    shared.userbot = userbot
    shared.plugin_manager = plugin_manager

    plugin_manager.load_plugins()
    userbot.loop.run_until_complete(userbot.send_message('me', 'TelDroid is Online!'))
    userbot.run_until_disconnected()
