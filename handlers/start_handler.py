from aiogram import types
from models import markup
from bot_setup import bot


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, text='Привет! Я бот.', reply_markup=markup.create_start_markup())
