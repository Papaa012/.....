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
         caption=f"""Há´Êâ¨ð¥ {msg.from_user.mention},

TÊÉªs Éªs {me2},
A sá´ÊÉªÉ´É¢ sá´ssÉªá´É´ É¢á´É´á´Êá´á´á´Ê Êá´á´, á´¡ÊÉªá´á´á´É´ ÉªÉ´ á´©Êá´Êá´É´ á´¡Éªá´Ê á´Êá´ Êá´Êá´© á´Ò á´©ÊÊá´É¢Êá´á´.
á´á´á´¡á´Êá´á´ ÊÊ â¨ð¥ : [ððð](https://t.me/iro_bot_support) !""",
Má´á´á´ á´¡Éªá´Ê ÊÊ : [ðððð¼ð¾ðð](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="â¨ É¢á´É´á´Êá´á´á´ sá´ssÉªá´É´ â£ï¸", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("â£ï¸ ððððððð â£ï¸", url="https://t.me/iro_x_support"),
                    InlineKeyboardButton("ð¥ ð¾ðð¼ðððð ð¥", url="https://t.me/iro_bot_support"),
                    InlineKeyboardButton("â¨ ðððð¼ð¾ðð â¨", user_id=OWNER_ID)
                ]
            ]
        ),
    )
