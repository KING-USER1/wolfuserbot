"""Check if userbot alive or not . """


import asyncio , time
from telethon import events
from userbot import StartTime
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, wolfversion , wolfdef
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname
import requests
import re
from PIL import Image
import os
import nekos

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "wolf"
WOLF_IMG = Config.ALIVE_PIC

@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await wolfdef.get_readable_time((time.time() - StartTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if WOLF_IMG:
         wolf_caption  = f"**Wolf User Bot ๐บ Running Fine**\n\n"
         wolf_caption += f"**โฮฑัฮฑะฒฮฑัั ััฮฑัฯั: (ใฃโโกโ)ใฃ โฅ Databases functioning normally!\n**"   
         wolf_caption += f"โฏ ๐๐๐ฅ๐๐ญ๐ก๐จ๐ง ๐ฏ๐๐ซ๐ฌ๐ข๐จ๐ง : `{version.__version__}\n`"
         wolf_caption += f"โฏ ๐๐๐ซ๐ฌ๐จ๐ง๐๐ฅ ๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐๐๐ซ๐ฌ๐ข๐จ๐ง : `{wolfversion}`\n"
         wolf_caption += f"โฏ ๐๐ฒ๐ญ๐ก๐จ๐ง ๐๐๐ซ๐ฌ๐ข๐จ๐ง : `{python_version()}\n\n`"
         wolf_caption += f"**๐'๐ฆ ๐ก๐๐ซ๐ ๐ญ๐จ ๐ก๐๐ฅ๐ฉ ๐ฒ๐จ๐ฎ, ๐ฆ๐ฒ ๐ฆ๐๐ฌ๐ญ๐๐ซ!\n**๐บ"
         wolf_caption += f"โฏ My Master: {DEFAULTUSER}\n"
         wolf_caption += f"โฏ uptime : `{uptime}\n"
         await borg.send_file(alive.chat_id, WOLF_IMG, caption=wolf_caption, reply_to=reply_to_id)
         await alive.delete()
    else:
        await alive.edit(f"**Wolf User Bot ๐บ Running Fine**\n\n"
                         "**โฮฑัฮฑะฒฮฑัั ััฮฑัฯั: (ใฃโโกโ)ใฃ โฅ Databases functioning normally!\n**" 
                         f"โฏ ๐๐๐ฅ๐๐ญ๐ก๐จ๐ง ๐ฏ๐๐ซ๐ฌ๐ข๐จ๐ง : `{version.__version__}\n`"
                         f"โฏ ๐๐๐ซ๐ฌ๐จ๐ง๐๐ฅ ๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐๐๐ซ๐ฌ๐ข๐จ๐ง : `{wolfversion}`\n"
                         f"โฏ ๐๐ฒ๐ญ๐ก๐จ๐ง ๐๐๐ซ๐ฌ๐ข๐จ๐ง : `{python_version()}\n\n`"
                         "**๐'๐ฆ ๐ก๐๐ซ๐ ๐ญ๐จ ๐ก๐๐ฅ๐ฉ ๐ฒ๐จ๐ฎ, ๐ฆ๐ฒ ๐ฆ๐๐ฌ๐ญ๐๐ซ!\n**๐บ"
                         f"โฏ My Master: {DEFAULTUSER}\n"
                         f"โฏ uptime : `{uptime}\n`"
                        )    

@borg.on(sudo_cmd(pattern="sudo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    uptime = await wolfdef.get_readable_time((time.time() - StartTime))
    await event.reply(" SUDO COMMANDS ARE WORKING PERFECTLY \n\n"
                      f"โฏ Telethon version: {version.__version__}\n"
                      f"โฏ Python: {python_version()}\n"
                      f"โฏ My peru owner: {DEFAULTUSER}\n"
                      f"**uptime :** `{uptime}\n`"
                      #"Deploy this userbot Now"
                     )

@borg.on(admin_cmd(pattern="wolf$"))
async def _(event):
    await event.delete() 
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.wolf()).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    img.seek(0)
    await bot.send_file(event.chat_id , open("temp.webp", "rb"),reply_to=reply_to_id) 
    
CMD_HELP.update({"alive": "`.alive` :\
      \n**USAGE:** Type .alive to see wether your bot is working or not.\
      \n\n`.wolf`\
      \n**USAGE : **Random wolf stickers"
}) 
