from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ✨🥀 {msg.from_user.mention},

Tʜɪs ɪs {me2},
sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Mᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ : [𝙋𝙄𝙆𝘼𝘾𝙃𝙐](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="✨ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ❣️", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 ❣️", url="https://t.me/iro_x_support"),
                    InlineKeyboardButton("🥀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 🥀", url="https://t.me/iro_bot_support"),
                    InlineKeyboardButton("✨ 𝙋𝙄𝙆𝘼𝘾𝙃𝙐 ✨", user_id=OWNER_ID)
