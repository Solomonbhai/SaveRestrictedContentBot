#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID =  17809227
API_HASH = '24c6288eee3e68db783afaf3df669534'
BOT_TOKEN = '5105784060:AAEuQbnUpzwHslcL_cyoArS5F1Q2IVtN_Qk'
SESSION = 'BQA50dDOyBFPh636_SkEnNvD99jiyG2Kr-plG5rl8FnHV7lQRH5y3eNCFrdj8DyuMkKt_j4Yln7OQ5by9CllgohCKeM4eNgfM2UzbVNi23fXNgPjnV3EZxcGyzIwm0qPdPBYo9tp5pd7vCUMc-uSaypocFbl7tsIGjChVVkyqitLD7Qv10wCCtlOgQCJQ9DaulPuQp-a0Hcv6dpFbod1pFPTTUMbo1GSWHJNv_LElkdDzsLjGy1DWWYx8ZgBqVtipTAoeMAV6xsvJDEjd22OGWa_pykc9p2TS2U_2RP_cBI-AjUD4udExQIAL2k6syPavgQrc2ozKwOR7Hja0hy0TD9eVFY_KAA'
FORCESUB = 'ffffswwwwgggd'
AUTH = 1414938408

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

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
    print(e)
    sys.exit(1)
