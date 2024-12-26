#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7692521610:AAHsfP1YKaGJY50PjML2NIPlLJagbAxOIz0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29707337"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a5277e625ace9924e1aedc0bd0800da4")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002086919404"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6810248021"))

#Port
PORT = os.environ.get("PORT", "8007")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://xrajputx5:yUtKHGMut90qKkIX@xrajputx5.tgk8kwm.mongodb.net/?retryWrites=true&w=majority&appName=xrajputx5")
DB_NAME = os.environ.get("DATABASE_NAME", "xrajputx5")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001920526810"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} , Thanks for using me :D @foxylinkk ⚡️.")
try:
    ADMINS = []
    raw_admins = os.environ.get("ADMINS", "6810248021‎")
    print(f"Raw ADMINS value: {raw_admins}")  # Debugging
    for x in raw_admins.split():
        sanitized = x.strip().replace("\u200e", "")  # Remove unwanted characters
        ADMINS.append(int(sanitized))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", " Hello {first}!\nPlease also Join our backup channel @foxylinkk")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "600"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "by @foxylinkk.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "for premium paid channel dm @primextg. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "@foxylinkk"

ADMINS.append(OWNER_ID)
ADMINS.append(6376328008)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
