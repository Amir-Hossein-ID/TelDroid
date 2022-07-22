from telethon import TelegramClient

import plugins

userbot: TelegramClient
plugin_manager: plugins.PluginManager
handler = "."
db = None

from shared.decorators import command
from shared.db import RedisDB, SQLiteDB
