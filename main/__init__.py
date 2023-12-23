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
SESSION = "BAC-G_qTYu_zrzHElVzpoCxXGsQF1P8RGezMvT81P_m2ALxhZEVVva2Oq6p8oce6PyMB-QyscO-2KuS7af4eGYzJ9FstnYFApmsTmS97A7ObXoI8ljO21fDS2EfgxWTREZ6SXhG5QD2oELLgg53OrFCSD4zqKucuvovvHQGrKs_l6eWCbu1XPweV-2KqzeULv-veK6hh9sF8hTrufext-HPH-bSGwSc84dvDAi6el_dLyvNmO7sR6yE8IYFFLXsUl24Fh8nuvhYC0-N-WwtGdRuCG1Grc27YlzyVHlAWvdyBG_DA2qPniYAsYt-m9e8Tx3ptZHS2sFBSe64jXv15GdP5AAAAAYSLfM0A" #config("SESSION", default=None)
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
