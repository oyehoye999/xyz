## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA8FMQi7VP_Fit_e7utDhAaT1OcFB6xtkMk7e7RyLyL-mDx9oU6st9T4f9FxyW0pw3qHw7a_faXc35YJipHDMHXVZYyis-dKFan0KfRyMfXQstPiutL_f9gfgI51GfnNkXPerUNHkkcUpisLIqErQHPSs4BtS5LluGH4mAnylmPIhYlCBsYmErLOjcolK-RYGagQer6Fp7ePSggshaHXjbZg7HH54tSPfo3QCDtB0ZPPYQSadqwVCzCWrdUEHeGaPn_mCLVYW_TZqaI8CHTO3pOlbu8m8pT9mbPdDsmCWXU5TVXER7LnD_RtE91Ue4exDQSC_UhqsWlOHIXEBaZMs_lAAAAAT2sfBkA")
BOT_TOKEN = getenv("BOT_TOKEN", "5468931327:AAGtFTfw42qHobf91iQD-6MWoZPZ55PnXnc")
BOT_NAME = getenv("BOT_NAME", "5468931327")
API_ID = int(getenv("API_ID", "19360347"))
API_HASH = getenv("API_HASH", "b73dee54ba45d3f9d1480f1be9f1339b")
OWNER_NAME = getenv("OWNER_NAME", "5329681433")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Romeo_RJ_143_music")
ALIVE_NAME = getenv("ALIVE_NAME", "5329681433")
BOT_USERNAME = getenv("BOT_USERNAME", "Romeo_RJ_music_1bot")
OWNER_ID = getenv("OWNER_ID", "5329681433")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "5329681433")
GROUP_SUPPORT = getenv("GROUP_SUPPORT" , "All_time_masti_official")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL" , "GirlboyDp143")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5329681433").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/oyehoye999/xyz")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/3f38eb0aec7ffc5cf6424.jpg")
