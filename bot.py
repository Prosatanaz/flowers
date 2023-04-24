from aiogram import types
from aiogram.dispatcher.filters import Command

from handlers.start_handler import start_handler
from aiogram.dispatcher import FSMContext
from aiogram import executor
from bot_setup import bot, dp

# настройка логирования


# регистрация хэндлеров
dp.register_message_handler(start_handler, commands=['start'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
