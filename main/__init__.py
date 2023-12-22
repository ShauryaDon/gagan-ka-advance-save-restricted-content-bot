#Github.com/mrinvisible7

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26075120" #config("API_ID", default=None, cast=int)
API_HASH = "1fda88a5d1de46058a4791c78bce198e" #config("API_HASH", default=None)
BOT_TOKEN = "6468925244:AAGOodGA2yOqZ_gtBATrmQvLpI1Aisl8VuI" #config("BOT_TOKEN", default=None)
SESSION = "BAASAviVFV5gxSg1-gIgSh0hMCCevs7yVcaAdK-UvQPZSqgzqTPWthWGRnaoMqZsE4jSAR9UHAiJO3qZMWzt2TRFDzLyY1gmK0Q5xcTnmP0-3OuYbCPObUpjfM5oc8z_XBgaCNjwr69I7PtzFp8ndu_fRcs4AZpHl654Vjh_KoJt7bWh1hsa4XeV65SDF2-Zr7gKk-mRTGWlFQIFybPxWmrYgf_GcI1KBv8QvQYB6fdaZ-N2oVlxUCd35uKUGzKBV_-IgGbEeYGIlf-5-TmMyTKAoA0R5yRxiAMwyNvx-06x1ta94DU5WFN91o_H7x9qBRVd_iLFO1EBgA75BeNF0O0kAAAAAYSLfM0A" #config("SESSION", default=None)
FORCESUB = "dev_gagan" #config("FORCESUB", default=None)
AUTH = "6876018655" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
