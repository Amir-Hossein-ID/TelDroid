import dotenv
import logging

import shared.startup

dotenv.load_dotenv()
logging.basicConfig(level=logging.WARNING)

shared.startup.start_bot()
