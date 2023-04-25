from bot_src.handlers.start_handler import start_handler
from aiogram import executor
from bot_setup import dp

# настройка логирования


# регистрация хэндлеров
dp.register_message_handler(start_handler, commands=['start'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
