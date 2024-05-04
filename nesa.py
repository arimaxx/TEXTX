import os
from telethon import TelegramClient, events, Button
import random
import asyncio
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_USERNAME = os.environ.get("BOT_USERNAME", "Legendmasbot")
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5957398316 6352061770").split()))
OWNER_ID = "6352061770"
LOG_ID = int(os.environ.get("LOGGER_ID", "-1001916618183"))
BOT_TOKEN = "6857479158:AAH8lJC_8huqEkb_B43w-CIJY09-XQNY4uE"

API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"

VIDEO_URLS = [
    "https://telegra.ph/file/1722b8e21ef54ef4fbc23.mp4",
    "https://telegra.ph/file/ac7186fffc5ac5f764fc1.mp4",
    "https://telegra.ph/file/4156557a73657501918c4.mp4",
    "https://telegra.ph/file/0d896710f1f1c02ad2549.mp4",
    "https://telegra.ph/file/03ac4a6e94b5b4401fa5a.mp4"
]
word_list = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

async def start_private_chat(event):
    video_url = random.choice(VIDEO_URLS)

    await event.respond(
        "<b>нυι</b> тнιѕ ιѕ 「🛡 ᴄᴏᴘʏʀɪɢʜᴛ ʜᴀɴᴅʟᴇʀ 🛡」❖ 💖\n"
        "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n"
        "ᴏᴜʀ ᴍɪssɪᴏɴ ɪs ᴛᴏ ᴇɴsᴜʀᴇ ᴀ  sᴇᴄᴜʀᴇ ᴀɴᴅ ᴘʟᴇᴀsᴇɴᴛ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ.\n "
        "ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴏ ᴍᴀɴᴛᴀɪɴɪɴɢ ᴅᴇᴄᴏʀᴜᴍ, ᴡᴇ'ᴠᴇ ɢᴏᴛ ɪᴛ ᴄᴏᴠᴇʀᴇᴅ.\n"
        "ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴀɴʏ ᴄᴏɴᴄᴇʀɴs, ᴀɴᴅ ʟᴇᴛ's ᴡᴏʀᴋ ᴛᴏɢᴇᴛʜᴇʀ ᴛᴏ ᴍᴀᴋᴇ ᴛʜɪs ᴄᴏᴍᴍᴜɴɪᴛʏ ᴛʜʀɪᴠᴇ\n"
        "❖ɴᴏ ᴄᴏᴍᴍᴀɴᴅ ᴊᴜꜱᴛ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ ɪs ᴀᴜᴛᴏ❖\n"
        "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n\n"
        "ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ [||ᴀʀɪ||❣️](https://t.me/lll_notookk_lll)",
        buttons=[
            [Button.url("❤️‍🔥ᴀᴅᴅ ᴍᴇ❤️‍🔥", f"https://t.me/{BOT_USERNAME}?startgroup=true"),
             Button.url("💫ꜱᴜᴘᴘᴏʀᴛ💫", f"https://t.me/{BOT_USERNAME}")],
            [Button.url("💖ꜱᴏᴜʀᴄᴇ💖", f"https://t.me/{BOT_USERNAME}")]
        ],
        parse_mode="html"
    )

async def delete_messages(event):
    message_text = event.raw_text.lower()

    if len(event.raw_text) > 1000 or any(word in message_text for word in word_list):
        await event.respond(f"{event.sender.username}'s message was deleted.")
        await event.delete()

async def main():
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        client.add_event_handler(start_private_chat, events.NewMessage(pattern='/start'))
        client.add_event_handler(delete_messages, events.NewMessage())
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
