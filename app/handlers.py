from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Добро пожаловать.', reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('С помощью данного бота вы можете разбогатеть')

@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.reply("Выберите категорию товара", reply_markup=kb.catalog)
    
@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию футболки')#, show_alert=True)
    