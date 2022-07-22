from telethon import TelegramClient

import logging

import plugins
from shared.decorators import command
from shared.db import RedisDB, SQLiteDB

userbot: TelegramClient
plugin_manager: plugins.PluginManager
handler = "."
db = None
logger = logging.getLogger()
