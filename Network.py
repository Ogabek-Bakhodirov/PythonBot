"""
 This is a echo bot.
 It echoes any incoming text messages.
 """
 
import logging
 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 
API_TOKEN = '6000921048:AAGKs6LcT7DbSY4Xq_oXVPYCe_hZCx8aR-k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

loginDatabase = ['log11']

btn_uzbek = KeyboardButton('/Uzbek')
btn_russia = KeyboardButton('/Russia')
languages = ReplyKeyboardMarkup(resize_keyboard=True)
hello = ReplyKeyboardMarkup()
languages.add(btn_uzbek)
languages.add(btn_russia)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/info` command
    """
    await message.reply("Hi!\nI'm a My Network 🚀 bot.\n"
                        "Choose the language ", reply_markup=languages)
    @dp.message_handler(commands='Uzbek')
    async def send_info(message: types.Message):
        await message.reply("hello")


if __name__ == '__main__':
    executor.start_polling(dp)