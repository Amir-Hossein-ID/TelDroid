import os

from telethon import TelegramClient
from telethon.sessions import StringSession

import plugins

userbot: TelegramClient
plugin_manager: plugins.PluginManager
handler = "."

from shared.startup import start_bot
from shared.decorators import command
