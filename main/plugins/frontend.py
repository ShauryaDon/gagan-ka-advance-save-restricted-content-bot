import time, os

import logging
import json
from .. import bot as gagan
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot

from telethon import events
from pyrogram.errors import FloodWait

#from ethon.telefunc import force_sub
from main.plugins.helpers import force_sub

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("telethon").setLevel(logging.INFO)

ft = f"To use this bot you've to join @{fs}."

message = "Send me the message link you want to start saving from, as a reply to this message."
          
process=[]
timer=[]
user=[]

# File path for storing authorized user IDs
SINGLE = 'single.json'

DON_ID = 6876018655

def loads_authorized_users():
    try:
        with open(SINGLE, 'r') as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

def saves_authorized_users(authorized_users):
    with open(SINGLE, 'w') as file:
        json.dump(list(authorized_users), file)

AUTHORIZED = loads_authorized_users()


@gagan.on(events.NewMessage(incoming=True, pattern='/sunauth'))
async def _unauth(event):
    """
    Command to revoke authorization for users
    """
    # Check if the command is initiated by the owner
    if event.sender_id == DON_ID:
        # Parse the user ID from the command
        try:
            user_id = int(event.message.text.split(' ')[1])
        except (ValueError, IndexError):
            return await event.respond("Invalid /unauth command. Use /unauth USER_ID.")

        # Remove the user ID from the authorized set
        if user_id in AUTHORIZED:
            AUTHORIZED.remove(user_id)
            saves_authorized_users(AUTHORIZED)
            await event.respond(f"Authorization revoked for user {user_id}.")
        else:
            await event.respond(f"User {user_id} is not authorized.")
    else:
        await event.respond("You are not authorized to use this command.")

# ... (your existing code)


@gagan.on(events.NewMessage(incoming=True, pattern='/sauth'))
async def _auth(event):
    """
    Command to authorize users
    """
    # Check if the command is initiated by the owner
    if event.sender_id == DON_ID:
        # Parse the user ID from the command
        try:
            user_id = int(event.message.text.split(' ')[1])
        except (ValueError, IndexError):
            return await event.respond("Invalid /auth command. Use /auth USER_ID.")

        # Add the user ID to the authorized set
        AUTHORIZED.add(user_id)
        saves_authorized_users(AUTHORIZED)
        await event.respond(f"User {user_id} has been authorized.")
    else:
        await event.respond("You are not authorized to use this command.")

@gagan.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    logging.info(event)
    file_name = ''
    
    # Check if the sender is authorized
    #if event.sender_id not in AUTHORIZED:
    #    return await event.reply("You are not authorized to use this bot.")
    
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    lit=event.text
    li=lit.split("\n")
    if len(li) > 10:
        await event.reply("max 10 links per message")
        return
    for li in li:
        #1239
    
        try:
            link = get_link(li)
            if not link:
                return
    
        except TypeError:
            return
        s, r = await force_sub(event.client, fs, event.sender_id, ft)
        if s == True:
            await event.reply(r)
            return
        edit = await event.reply("Processing!")
        if f'{int(event.sender_id)}' in user:
            return await edit.edit("Please don't spam links, wait until ongoing process is done.")
        user.append(f'{int(event.sender_id)}')
        if "|" in li:
            url = li
            url_parts = url.split("|")
            if len(url_parts) == 2:
            
                file_name = url_parts[1]
        if file_name is not None:
            file_name = file_name.strip()                
        try:
            if 't.me/' not in link:
                await edit.edit("invalid link")
                ind = user.index(f'{int(event.sender_id)}')
                user.pop(int(ind))
                return
            if 't.me/+' in link:
                q = await join(userbot, link)
                await edit.edit(q)
                ind = user.index(f'{int(event.sender_id)}')
                user.pop(int(ind))
                return
            if 't.me/' in link:
                msg_id = 0
                try:
                    msg_id = int(link.split("/")[-1])
                except ValueError:
                    if '?single' in link:
                        link_ = link.split("?single")[0]
                        msg_id = int(link_.split("/")[-1])
                    else:
                        msg_id = -1
                m = msg_id
                await get_msg(userbot, Bot, event.sender_id, edit.id, link, m, file_name)
        except FloodWait as fw:
            await gagan.send_message(event.sender_id, f'Try again after {fw.value} seconds due to floodwait from telegram.')
            await edit.delete()
        except Exception as e:
            logging.info(e)
            await gagan.send_message(event.sender_id, f"An error occurred during cloning of `{link}`\n\n**Error:** {str(e)}")
            await edit.delete()
        ind = user.index(f'{int(event.sender_id)}')
        user.pop(int(ind))
        time.sleep(1)
