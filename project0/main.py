from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

API_KEY = '5699527558:AAGtfCXqGB5fDqcByRpNTq2rPZzcUbIh504'
dp = Bot(token=API_KEY)
bot = Dispatcher(dp)
button1 = KeyboardButton("youtube")
button2 = KeyboardButton("something!")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.add(button1)
keyboard1.add(button2)

@bot.message_handler( commands=['start','Start'] )
async def start(message):
    await message.reply("safsaf",reply_markup = keyboard1)

@bot.message_handler(func=lambda msg: msg)
async def normal_message_handler(message):  
    if  message.text=="something!":
        bot.reply_to(message, "hello motha fuka")  #"hello motha fuka"
    elif message.text=="youtube":
        bot.reply_to(message, "hi youtube")  #"youtube"
    else:
        bot.reply_to(message, message.text)  #"hello motha fuka"


executor.start_polling(bot)

