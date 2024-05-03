import os
import random
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_USERNAME = os.environ.get("BOT_USERNAME", "Legendmasbot")
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5957398316 6352061770").split()))
OWNER_ID = "6352061770"
LOG_ID = int(os.environ.get("LOGGER_ID", "-1001916618183"))
TOKEN = "6857479158:AAH8lJC_8huqEkb_B43w-CIJY09-XQNY4uE"

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

lock_file_path = "bot.lock"

async def start_private_chat(bot, message):
    video_url = random.choice(VIDEO_URLS)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️‍🔥ᴀᴅᴅ ᴍᴇ❤️‍🔥", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
                InlineKeyboardButton("💫ꜱᴜᴘᴘᴏʀᴛ💫", url=f"t.me/{BOT_USERNAME}"),
            ],
            [
                InlineKeyboardButton("💖ꜱᴏᴜʀᴄᴇ💖", url=f"t.me/{BOT_USERNAME}"),
            ]
        ]
    )

    await bot.send_video(
        chat_id=message.chat.id,
        video=video_url,
        caption="<b>нυι</b> тнιѕ ιѕ 「🛡 ᴄᴏᴘʏʀɪɢʜᴛ ʜᴀɴᴅʟᴇʀ 🛡」❖ 💖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n"
                "ᴏᴜʀ ᴍɪssɪᴏɴ ɪs ᴛᴏ ᴇɴsᴜʀᴇ ᴀ  sᴇᴄᴜʀᴇ ᴀɴᴅ ᴘʟᴇᴀsᴇɴᴛ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ.\n "
                "ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴏ ᴍᴀɴᴛᴀɪɴɪɴɢ ᴅᴇᴄᴏʀᴜᴍ, ᴡᴇ'ᴠᴇ ɢᴏᴛ ɪᴛ ᴄᴏᴠᴇʀᴇᴅ.\n"
                "ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴀɴʏ$@$v=v1.16$@$ᴄᴏɴᴄᴇʀɴs, ᴀɴᴅ ʟᴇᴛ's ᴡᴏʀᴋ ᴛᴏɢᴇᴛʜᴇʀ ᴛᴏ ᴍᴀᴋᴇ ᴛʜɪs ᴄᴏᴍᴍᴜɴɪᴛʏ ᴛʜʀɪᴠᴇ\n"
                "❖ɴᴏ ᴄᴏᴍᴍᴀɴᴅ ᴊᴜꜱᴛ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ ɪs ᴀᴜᴛᴏ❖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n\n"
                "ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ <a href=\"https://t.me/lll_notookk_lll\">||ᴀʀɪ||❣️</a>",
        reply_markup=keyboard
    )

async def start(update: Update, context):
    await start_private_chat(context.bot, update.message)

async def delete_messages(update: Update, context):
    message_text = update.message.text.lower()

    if update.edited_message or len(update.message.text) > 1000 or any(word in message_text for word in word_list):
        user_mention = f"@{update.message.from_user.username}" if update.message.from_user.username else update.message.from_user.first_name
        context.bot.send_message(chat_id=update.message.chat_id, text=f"{user_mention}'s message was deleted.")
        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

def main():
    if os.path.exists(lock_file_path):
        logger.warning("Another instance is already running. Exiting...")
        return

    with open(lock_file_path, "w") as lock_file:
        lock_file.write("locked")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, delete_messages))

    updater.start_polling()

    updater.idle()

    os.remove(lock_file_path)

# Example start for Telethon
async def start_telethon():
    # Your Telethon code here
    pass

if __name__ == '__main__':
    asyncio.run(start_telethon())
    main()
