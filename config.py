## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCtKFWEBg82PfVBPc1i1TQtVN_StW5u5Wg2-3apGb6XrFPugu56RlP83jA-ENhYlf-1Ylws36ZoroVLolrxWm7dgdt7pRYQJawF9C9F-C9_PP0RWernYpTEyMUkxKU7er4crjEhGw4ILbDdRLYwA6Ul8q_4Qc-9VkJo_HOLJnTg5XH4lVjEG3Ue2ZxB3nqPqK8g49paf2AmqoV8VHqTL7ebdFMGFmhLj9Iw55JbAvLNrR4TqK11Ax4O7sRYiljQ1tj_MvKu2cZTn8VccVFpz4eoV6cOSUNgSOO2D7ZN9qxl-RgHEKJEqMDC_FoagNex2ZUyYUee82xqWeln1ATj-EFoAAAAAT2sfBkA")
BOT_TOKEN = getenv("BOT_TOKEN", "5468931327:AAGtFTfw42qHobf91iQD-6MWoZPZ55PnXnc")
BOT_NAME = getenv("BOT_NAME", "5468931327")
API_ID = int(getenv("API_ID", "19360347"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "5329681433")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Romeo_RJ_143_music")
ALIVE_NAME = getenv("ALIVE_NAME", "5329681433")
BOT_USERNAME = getenv("BOT_USERNAME", "Romeo_RJ_music_1bot")
OWNER_ID = getenv("OWNER_ID", "5329681433")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "5329681433")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5329681433").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/oyehoye999/xyz")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
