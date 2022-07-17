## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABBpaCsH0S2tJm7dDQx5OJBbPoYLgcExeIfNl0_SHcDVtdvF-pXeHo9HX_L0UpQS9Yw-vaqJTXSn7vEPjGdeAlFtghlvr6Es0Tt8cY1Bq60zjgmAnc2fjnet-LgFQyXT5ByDBU3-1T00U3yKEyBZWxh0ed0XUKY9Ks0q88UYrOiDmNyDked56lDNc07VCr3zeGhllPc1xdCUuf0vDN2LxR1xDY7CEJ3JD3k7NFf6gVw3fogyAyTiL7d66YZdxfTBZTtAxCaNTGsGZur0aRIB86EJ2G_dU7OuP4AqDFcSk-25TJiFFRky60dEDTmdUkvXGNcWD3UHs6mnio9UZmK-oWVAAAAATmgx1UA")
BOT_TOKEN = getenv("BOT_TOKEN", "5552040060:AAGHil9JchhWal_8FT24B_vic9qrKqhWPVk")
BOT_NAME = getenv("BOT_NAME", "rodee58")
API_ID = int(getenv("API_ID", "12984285"))
API_HASH = getenv("API_HASH", "6ff4ebeaefc9ab8b963f9eddf7f54be3")
OWNER_NAME = getenv("OWNER_NAME", "anas")
OWNER_USERNAME = getenv("OWNER_USERNAME", "anaskn58")
ALIVE_NAME = getenv("ALIVE_NAME", "anas")
BOT_USERNAME = getenv("BOT_USERNAME", "rodee58bot")
OWNER_ID = getenv("OWNER_ID", "5261805397")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5261805397").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://t.me/rodee_58")
START_PIC = getenv("START_PIC", "https://t.me/rode_58")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
