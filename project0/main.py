from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from requests import *
import os
import pyqrcode
import rpc as g
API_KEY = os.getenv('API_KEY')
dp = Bot(token=API_KEY)
bot = Dispatcher(dp)

button1 = InlineKeyboardButton(text="👋 LOW", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="💋 High", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
#inline doesnt send message it sends callback data (read by bot.callback_query_handler(text=[]))
kerboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hello!", "💋 Youtube")
#reply keyboard much better option

kerboard_rps = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add("rock!", "paper!", "sissors!").add("exit")

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
    #g.games(message)

@bot.message_handler(commands=['pic', 'Pic'])
async def pics(message: types.Message):
    await message.answer_photo("https://pbs.twimg.com/profile_images/1566268560023977984/zahVS0ZW_400x400.jpg")

@bot.message_handler(commands=["qr"])
async def qr(message: types.Message):
    text = pyqrcode.create("qr")#pyqrcode.create(message.text)
    text.png('test.png', scale=5)
    await dp.send_photo(chat_id=message.chat.id, photo=open('test.png', 'rb'))
    

randomPImageUrl ="https://picsum.photos/1200"
randomPeopleUrl ="https://thispersondoesnotexist.com/image"
@bot.message_handler(commands=["randomPImage"])
async def locpics(message: types.Message):
    await dp.send_photo(chat_id=message.chat.id, photo = get(randomPImageUrl).content )
    #if we use just the url it will show same pic twice
@bot.message_handler(commands=["randomPeople"])
async def locpics(message: types.Message):
    await dp.send_photo(chat_id=message.chat.id, photo = get(randomPeopleUrl).content )    


@bot.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("hello motha fuka")
    elif message.text == '💋 Youtube':
        await message.reply("https://youtube.com")
    
    else:
        await message.reply(f"Your message is: {message.text}")

executor.start_polling(bot)