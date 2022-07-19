import os

from telethon import TelegramClient
from telethon.sessions import StringSession

import plugins
import shared

def start_bot():
    userbot = TelegramClient(StringSession(os.getenv('SESSION_STRING')), os.getenv('API_ID'), os.getenv('API_HASH'))
    userbot.start()
    plugin_manager = plugins.PluginManager()

    shared.userbot = userbot
    shared.plugin_manager = plugin_manager

    plugin_manager.load_plugins()
    userbot.loop.run_until_complete(userbot.send_message('me', 'TelDroid is Online!'))
    userbot.run_until_disconnected()
