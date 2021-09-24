from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**merhaba, ben {bn} 🎵

Ben sesli sohbetlerde müzik çalmanıza yarayan bir botum. Kendinize Bot yapmak için [ADSIZ KAPTAN](https://t.me/kizilsancaksahibi).

Beni gruba yönetici olarak ekleyiniz!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Kaynak Sahibi 🛠", url="https://t.me/kizilsancaksahibi")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/smailesi"
                    ),
                    InlineKeyboardButton(
                        "🔊 Ücretli İşlemler", url="https://t.me/kizilsancakbilgi"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/ellycarlmusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Elly Carl a aşık ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Ücretli İşlemler", url="https://t.me/kizilsancakbilgi")
                ]
            ]
        )
   )


