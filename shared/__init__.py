from telethon import TelegramClient

import plugins

userbot: TelegramClient
plugin_manager: plugins.PluginManager
handler = "."

from shared.decorators import command
