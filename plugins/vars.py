import os

API_ID    = os.environ.get("API_ID", "29171167")
API_HASH  = os.environ.get("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
