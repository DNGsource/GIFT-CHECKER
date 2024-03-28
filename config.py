from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
API_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("APP_HASH")
token = os.environ.get("TOKEN")
admin = os.environ.get("ADMIN")
client = TelegramClient('BotSession', API_ID, API_HASH).start(bot_token=token)
bot = client
bot.start()