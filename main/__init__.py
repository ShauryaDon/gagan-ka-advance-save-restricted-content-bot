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
API_HASH = "1fda88a5d1de46058a4791c78bce198e" config("API_HASH", default=None)
BOT_TOKEN = " config("BOT_TOKEN", default=None)
SESSION = "BAGTAMIAkuo6zxvXfkuOUev2_eTObuSpIy64jUNGyiOOV9ibWhxFQaQnMySC9dquC3qgPB4Xjm2S96QCLrAUTm7_LY5a2alxD8obzhFznf-0v2nF-HuaFnmeQcxdiX1lIKt3Wy-by7Wp9TpLQjz6liGLkvZfzXbt69jFxew2BxpkuVcD5KhTSUYdYwEr9B0F-CtbhuvKyeyakQwESOsl8_VKx9uPivyHzgDn-z2wnKzOYr2xWC5riKkPGaZDN4X-8_4CJNogu_6QGDHAtbX6SlJhMWgHyjL_I27kyWUWgpP7JRHsUbS0_8XaMYkccwgrwtG7Iz1oZHUZegtjQqge9dbZtEOVzAAAAAF_8NGXAA" #config("SESSION", default=None)
FORCESUB = "dev_gagan2" #config("FORCESUB", default=None)
AUTH = "6964148334" #config("AUTH", default=None)
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
    print("Your session expired please re add that... thanks @dev_gagan.")
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
