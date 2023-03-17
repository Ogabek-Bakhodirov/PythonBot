import logging
 
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '6000921048:AAGKs6LcT7DbSY4Xq_oXVPYCe_hZCx8aR-k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

loginDatabase = ['log11']

@dp.message_handler(commands=['start', 'info'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/info` command
    """
    await message.reply("Hi!\nI'm a My Network 🚀 bot.\nI can help you to solve issues with your Wifi connection or problems with your router.\nSend me one of them\n /checkConnection \n /balans")

@dp.message_handler()
async def echo(message: types.Message):
#    old style:
#     await bot.send_message(message.chat.id, message.text)
    for i in loginDatabase:
        if i == message.text:
            await message.reply("Log in done succesfully")
            return
    await message.answer('Log in did not found!')

@dp.message_handler(commands=['checkConnection'])
async def send_welcome(message: types.Message):
    await message.reply("Please enter your log in.")

@dp.message_handler(commands=['balans'])
async def send_welcome(message: types.Message):
    await message.reply("Please enter your log in and password.")

# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('/Users/ogabekbakhodirov/Documents/Python/PythonBot/catImage.jpeg', 'rb') as photo:
#         '''
#         # Old fashioned way:
#         await bot.send_photo(
#             message.chat.id,
#             photo,
#             caption='Cats are here 😺', 
#             reply_to_message_id=message.message_id,
#         )
#         '''

#         await message.reply_photo(photo, caption='Cats are here 😺')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    print("Hello world")