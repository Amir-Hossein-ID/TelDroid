import dotenv
import logging

import shared

dotenv.load_dotenv()
logging.basicConfig(level=logging.WARNING)

shared.start_bot()

shared.userbot.run_until_disconnected()
