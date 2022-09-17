from aiogram import bot, dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

API_KEY = '5699527558:AAGtfCXqGB5fDqcByRpNTq2rPZzcUbIh504'
dp = telebot.TeleBot(token=API_KEY)
bot = Dispatcher(dp)
button1 = KeyboardButton("youtube")
button2 = KeyboardButton("something!")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.add(button1)
keyboard1.add(button2)

@bot.message_handler(commands=['start','Start')


executor.start_polling(bot)

