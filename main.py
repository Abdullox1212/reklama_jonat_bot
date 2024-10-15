import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7918812657:AAHnmhxoUEpZVe10vnEJNo9zQGw4vcLkXXA'
CHAT_ID = '-1002124525737'  # Guruh chat ID sini bu yerga yozing

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Matn yuboruvchi funksiyani yaratamiz
async def send_message_periodically():
    while True:
        await bot.send_photo(CHAT_ID, caption="""
<b><i>👋 Assalomu alayko'm aziz guruhimiz a'zolari❗️</i></b>

<b>Biz Yangi konkursga start berdik 🎉 🎁🎁 </b>

<i>Kunkurs Shartlari ✅:</i>

<i>Qachonki guruhimizda a'zolar soni <b>1000</b>taga teng bo'lsa, shu kuni sizning orangizdan <b>10ta omadli inson</b>ni tanlab olamiz va ularga 1 oylik tekinga botdan foydalanush huquqini beramiz🤑</i>

<b>Hammamiz 5tadan odam qo'shsak ham, 1kunda bo'lamiz👌

10ta omadli insonlarning ichida albatta siz ham borsiz🫵


Albatta hamma qatnashishini so'rab qolamiz❗️

OMAD✊</b>

""", photo="https://t.me/DASSU_UZ/126")
        await asyncio.sleep(1200)  # 1800 sekund = 30 daqiqa



@dp.message_handler()

async def send_message(message: types.Message):
    print(message.text)

# Botni ishga tushirish
async def on_startup(_):
    asyncio.create_task(send_message_periodically())  # Xabar yuborishni boshlash

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


