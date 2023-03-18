import logging
from enum import Enum
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
 
#  KEY
API_TOKEN = '6000921048:AAGKs6LcT7DbSY4Xq_oXVPYCe_hZCx8aR-k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Keyboard

# Set up language buttons
def setupLangButtons():
    uzbekLang = KeyboardButton("Uzbek 🇺🇿")
    rusLang = KeyboardButton("Rus 🇷🇺")
    keyboardLang = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(uzbekLang).add(rusLang)
    return keyboardLang

# Set up menu action buttons
def setupMenuActionButtons():
    balanceBTN = KeyboardButton('Check balance 💸')
    connectionBTN = KeyboardButton('Check connection 📶')
    keyboardLang = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(balanceBTN).add(connectionBTN)
    return keyboardLang

@dp.message_handler(commands=['start', 'info'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm a My Network 🚀 bot.\nI can help you to solve issues with your Wifi connection or problems with your router.")
    await message.reply("Please choose language that you prefer", reply_markup=setupLangButtons() )


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "Uzbek 🇺🇿":
        await message.reply("Qonday")
    elif message.text == "Rus 🇷🇺":
        await message.reply("Privet")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
