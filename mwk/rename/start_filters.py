import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

if bool(os.environ.get("WEBHOOK", False)):
    from mwk.config import Config
else:
    from config import Config

# the Strings used for this "thing"
from mwk.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("help"))
async def help_user(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "banned":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D** to Use Me. If you feel it's a Fault contact @TeleRoid14")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**Join My Updates Channel to use me & Enjoy the Free Service**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join Our Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    await m.reply_text(Translation.HELP_USER.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("⭕ BᴏᴛLɪsᴛ ⭕", url=f"https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                    InlineKeyboardButton("💢 Gɪᴛʜᴜʙ", url=f"https://github.com/PredatorHackerzZ/Renamer-Bot")
                ],
                [
                InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ", url=f"https://t.me/TheTeleRoid"),
                    InlineKeyboardButton("🚸 Pᴏᴡᴇʀᴇᴅ Bʏ", url=f"https://t.me/MoviesFlixers_DL")
                ]
            ]
        ),
        reply_to_message_id=m.message_id
    )
          #  return

@Client.on_message(filters.command("about"))
async def about_bot(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "banned":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D** to Use Me. If you feel it's a Fault contact @TeleRoid14")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**Join My Updates Channel to use me & Enjoy the Free Service**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join Our Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    await m.reply_text(Translation.ABOUT_BOT.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("⭕ BᴏᴛLɪsᴛ ⭕", url=f"https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                    InlineKeyboardButton("💢 Gɪᴛʜᴜʙ", url=f"https://github.com/PredatorHackerzZ/Renamer-Bot")
                ],
                [
                InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ", url=f"https://t.me/TheTeleRoid"),
                    InlineKeyboardButton("🚸 Pᴏᴡᴇʀᴇᴅ Bʏ", url=f"https://t.me/MoviesFlixers_DL")
                ]
            ]
        ),
        reply_to_message_id=m.message_id
    )
          #  return

@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "banned":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel it's a fault contact @TeleRoid14")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**Join My Updates Channel to use me & Enjoy the Free Service**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join Our Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    await m.reply_text(Translation.START_TEXT.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("⭕ Cʜᴀɴɴᴇʟ ⭕", url=f"https://t.me/TeleRoidGroup"),
                    InlineKeyboardButton("⭕ Sᴜᴘᴘᴏʀᴛ ⭕", url=f"https://t.me/TeleRoid14")
                ],
                [
                InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ", url=f"https://t.me/TheTeleRoid"),
                    InlineKeyboardButton("🚸 Pᴏᴡᴇʀᴇᴅ Bʏ", url=f"https://t.me/MoviesFlixers_DL")
                ],
                [
                    InlineKeyboardButton("🔐 Cʟᴏsᴇ ", callback_data="cancel")
                ]
            ]
        ),
        reply_to_message_id=m.message_id
    )
          #  return
        
@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
