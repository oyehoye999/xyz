import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(5329681433)
    ":memory:",
    API_ID,19360347
    API_HASH,b73dee54ba45d3f9d1480f1be9f1339b
    bot_token=BOT_TOKEN,5468931327:AAGtFTfw42qHobf91iQD-6MWoZPZ55PnXnc
    plugins={"root": "Zaid.Player"},
)

BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

user = Client(5329681433)
    SESSION_NAME,BQDCjr4AT_-nALZTn_ug6jF_dwrwW_E5dDweBuK4ZLi1xyqJDJFGt09WzMn8-1DTVphS2ulRAK7JJFQE0Py0IWbskVnDbkRiFBDWW7Q989zpNIkTZOuK0koESI5gsY7ChviWE49xzF9NaMacO-p8xRSaWbBzzu6JOGXqukQRlqgHwqJhROTkrzcjIKj_szaC1SZW3Vx0G5p666J4bTHbyoOH78uWpuMwPEw4gR8rB5YJLIac0ns51JfLX_hjYc3xi4WkNmim76KbGEfRXu9v_aqqMRAHD1ig6TGN1Ku5OESNwrNMzXfHEFMApQDjGeCkFCrI3g-SCTb399_1FqRK4r_8AAAAAT2sfBkA
    api_id=API_ID,19360347
    api_hash=API_HASH,b73dee54ba45d3f9d1480f1be9f1339b
)

Test = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'Zaid.Player'})
call_py = PyTgCalls(
    Test,
    cache_duration=100,
    overload_quiet_mode=True,
)
