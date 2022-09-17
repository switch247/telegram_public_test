from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import main as m

dp = Bot(token='5699527558:AAGtfCXqGB5fDqcByRpNTq2rPZzcUbIh504')
bot = Dispatcher(dp)



kerboard_rps = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add("rock!", "paper!", "sissors!").add("exit")
options=["rock!", "paper!", "sissors!"]
@bot.message_handler(commands=['start', 'Start'])
async def welcome(message: types.Message):
    await message.reply("Hello!", reply_markup=kerboard_rps)
    playing=False
    while(playing):
    @bot.send_message(text="sdf",reply_markup=kerboard_rps)

@bot.message_handler( func = lambda msg: msg in ["rock!", "paper!", "sissors!","exit"])
async def games(message):
    x = options[randint(0, 2)]
    if message.text == 'rock!':
        await message.reply ( x , reply_markup=kerboard_rps)

    elif message.text == 'paper!':
         await message.reply( x , reply_markup=kerboard_rps)

    elif message.text == 'sisors!':
        await message.reply( x , reply_markup=kerboard_rps )

    elif message.text == 'exit':
        return
    await message.reply ( winner(message,x) )
def winner(u,b):
    if u=='rock!' and b=='sissors!':
        return("WIN!!!")
    elif u == 'paper!' and b=='rock!':
        return("WIN!!!")
    elif u == 'sissors!' and b =='paper!':
        return("WIN!!!")
    elif u==b:
        return "DRAW!!"
    else:
        return "LOSE!"





executor.start_polling(bot)