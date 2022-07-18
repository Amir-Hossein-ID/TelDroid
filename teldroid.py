import asyncio
import os

from telethon import TelegramClient
from telethon.sessions import StringSession

import dotenv
import logging

dotenv.load_dotenv()
logging.basicConfig(level=logging.WARNING)

userbot = TelegramClient(StringSession(os.getenv('SESSION_STRING')), os.getenv('API_ID'), os.getenv('API_HASH'))
userbot.start()

asyncio.get_event_loop().run_until_complete(userbot.send_message('me', 'Deployed!'))
userbot.run_until_disconnected()
