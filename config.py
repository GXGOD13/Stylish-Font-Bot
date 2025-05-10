import os
from typing import List

API_ID = os.environ.get("API_ID", "21769517")
API_HASH = os.environ.get("API_HASH", "a18bca05e643355610f88e15425287a7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7562079827"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002580205471"))

DB_URI = os.environ.get("DB_URI", "mongodb+srv://gxmon239:f4l7bKrhka3Fh2cV@cluster0.qmblwql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002553401644").split()))  # Add Multiple channel id's
