from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import FSInputFile
from random import randint

dp = Bot(token='5699527558:AAGtfCXqGB5fDqcByRpNTq2rPZzcUbIh504')
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

@bot.message_handler(commands=['pic', 'Pic'])
async def pics(message: types.Message):
    await message.answer_photo("https://avatars.githubusercontent.com/u/62240649?v=4")

@bot.message_handler(commands=['lpic', 'lPic'])
async def locpics(message: types.Message):
    
    await bot.send_photo(chat_id=message.chat.id, photo = FSInputFile('project0\pics\images.jpg') )#open('project0\pics\images.jpg', 'rb')
    


@bot.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("hello motha fuka")
    elif message.text == '💋 Youtube':
        await message.reply("https://youtube.com")
    
    else:
        await message.reply(f"Your message is: {message.text}")



executor.start_polling(bot)







