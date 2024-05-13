import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

load_dotenv()

token = os.getenv("TOKEN")

bot = Bot(token=token)
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply("Как дела?")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot is starting")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')