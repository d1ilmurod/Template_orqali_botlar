import asyncio

from aiogram import types
from data.config import ADMINS
from loader import dp,db,bot


@dp.message_handler(text = '/allusers',user_id = ADMINS)
async def get_user_all(msg: types.Message):
    users = db.select_all_users()
    #print(users[0][0])
    await msg.answer(users)

@dp.message_handler(text = '/reklama',user_id = ADMINS)
async def send_ad_to_all(msg: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id,text="Yordam qiling akajonlar")
        await asyncio.sleep(0.05)


@dp.message_handler(text='/cleandb',user_id=ADMINS)
async def get_all_users(msg: types.Message):
    db.delete_users()
    await msg.answer("Baza tozalandi!")
