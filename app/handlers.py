from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Добро пожаловать.', reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('С помощью данного бота вы можете разбогатеть')

@router.message(F.text == "nice")
async def cmd_nice(message: Message):
    await message.reply('Я рад это слышать!')
