#    Copyright (C) Midhun KM 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
from googletrans import Translator
import re
from math import ceil
from userbot.plugins import inlinestats
from telethon import custom, events, Button
from userbot import CMD_LIST
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from userbot import Lastupdate, bot
from userbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid, add_usersid_in_db, get_all_users

@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    vent = event.chat_id
    starttext = ("Hi! this is An Assistant Bot For My [Owner] ")
    if event.from_id == bot.uid:
        await tgbot.send_message(
           vent,
           message="Hi Master, It's Me Your Assistant.",
           buttons = [
           [custom.Button.inline("Broadcast 🔥", data="mebroadcast")],
           [Button.url("Repo?", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
            ]
           )
    else:
        await tgbot.send_message(
           event.chat_id,
           message=starttext,
           link_preview=False,
           buttons = [
           [custom.Button.inline("Deploy your Friday 🇮🇳", data="deploy")],
           [Button.url("Help Me ❓", "t.me/Fridayot")]
       ]
      )


# Data's

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
        await event.delete()
        if event.query.user_id is not bot.uid:
            await tgbot.send_message(
                event.chat_id,
                message="You Can Deploy Friday In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
                buttons = [
                [Button.url("Deploy Tutorial 📺", "https://youtu.be/xfHcm_e92eQ")],
                [Button.url("Need Help ❓", "t.me/FridaySupportOfficial")]
                 ]
                )

# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    ignore = ['/start', '/tr', '/ping', 'fuck', 'madarchod']
    sedlyfvro = event.raw_text
    if any(a in event.raw_text for a in ignore):
        pass
    elif event.chat_id == bot.uid:
        pass
    else:
        sender = await event.get_sender()
        chat_id = event.chat_id
        sed = await event.forward_to(bot.uid)
        

# Add User To Database ,Later For Broadcast Purpose
# (C) @SpecHide
        add_me_in_db(
            sed.id,
            event.from_id,
            event.id
        )

        add_usersid_in_db(
            event.from_id
        )



# Test 
@tgbot.on(events.NewMessage)
async def sed(event):
        if event.from_id == bot.uid:
            msg = await event.get_reply_message()
            real_nigga = msg.id
            user_id, reply_message_id = his_userid(
            msg.id
            )
            await event.send_message(
            user_id
        )
        else:
            pass


# broadcast
@tgbot.on(events.NewMessage(pattern="^/broadcast ?(.*)"))
async def sedlyfbro(event):
         if event.from_id == bot.uid:
             msgtobroadcast = event.pattern_match.group(1)
             userstobc = get_all_users()
             error_count = 0
             sent_count = 0
         for userstobc in userstobc:
             try:
                 sent_count += 1
                 await tgbot.send_message(int(userstobc.chat_id), msgtobroadcast)
                 await tgbot.send_message(
                 bot.uid,
                 f"Sent : {sent_count}\nError : {error_count}\nTotal : {len(userstobc)}",
             )
         except Exception as starkerror:
             await tgbot.send_message(
             bot.uid,
             f"Error : {error_count}\nError : {starkerror} \nUsers : {chat_id}",
         )
         else: 
             pass
                 
