from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
def create_start_markup():
    # создаем кнопку
    start_button = InlineKeyboardButton('Старт', web_app=WebAppInfo(url='https://chat.openai.com/'))
    # создаем клавиатуру и добавляем кнопку
    start_keyboard = InlineKeyboardMarkup().add(start_button)
    return start_keyboard