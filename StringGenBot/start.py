from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    alt = await bot.get_me()
    me2 = alt.mention
    await bot.send_photo(
        chat_id=msg.chat.id,
         photo="https://telegra.ph/file/e71b24bf65a37ecbf5a22.jpg",
         caption=f"""Hᴇʏ✨🥀 {msg.from_user.mention},

Tʜɪs ɪs {me2},
A sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
ᴘᴏᴡᴇʀᴇᴅ ʙʏ ✨🥀 : [𝙄𝙍𝙊](https://t.me/iro_bot_support) !""",
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
                ]
            ]
        ),
    )
