from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

dp = Bot(token='5699527558:AAGtfCXqGB5fDqcByRpNTq2rPZzcUbIh504')
bot = Dispatcher(dp)

button1 = InlineKeyboardButton(text="👋 LOW", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="💋 High", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
#inline doesnt send message it sends callback data (read by bot.callback_query_handler(text=[]))
kerboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hello!", "💋 Youtube")
#reply keyboard much better option

kerboard_rps = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("rock!", "paper!", "sissors!")
@bot.message_handler(commands=['start', 'Start'])
async def welcome(message: types.Message):
    await message.reply("Hello!", reply_markup=kerboard_reply)




@bot.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)
    
@bot.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer(randint(1, 10))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    await call.answer()



@bot.message_handler(commands=['Game', 'game'])
async def play(message: types.Message):
    await message.reply("you want to Blay lets Blay", reply_markup=kerboard_rps)
    options=["rock!", "paper!", "sissors!"]
    @bot.message_handler()
    async def games(message):
        x=options[randint(0, 2)]
        if message.text == 'rock!':
            await message.reply (  x )

        elif message.text == 'paper!':
            await message.reply( x )

        elif message.text == 'sisors!':
            await message.reply( x  )

        elif message.text == 'exit':
            return
        winner(message,x)
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



@bot.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("hello motha fuka")
    elif message.text == '💋 Youtube':
        await message.reply("https://youtube.com")
    
    else:
        await message.reply(f"Your message is: {message.text}")



executor.start_polling(bot)







