try:
    import telethon
except ImportError:
    print("Installing Telethon...\n\n")
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
    try:
        import telethon
    except ImportError:
        print("Telethon installation failed. Try to install it manually, then run this script again.")
        sys.exit(1)


from telethon.sessions import StringSession
from telethon.sync import TelegramClient

API_ID = int(input("Enter your API ID(Integer): "))
API_HASH = input("Enter your API HASH: ")

try:
    with TelegramClient(StringSession(), API_ID, API_HASH) as userbot:
            ses = userbot.session.save()
            userbot.send_message("me",f"Your `SESSION`:\n\n`{ses}`\n\n**Do not share this anywhere!**\n@TelDroid")
            print("Your Session:\n")
            print(ses)
            print("\nIt was also sent to your SAVED MESSAGES in Telegram")
except:
	print("Something went wrong, recheck api_id, api_hash and phone number then try again")
