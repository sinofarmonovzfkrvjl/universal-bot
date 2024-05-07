from aiogram import Bot, Dispatcher, types
from asyncio import run
import logging
from deep_translator import GoogleTranslator
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from keyboards import languages_button, database, menus_button
from states import Translate
from aiogram.client.session.aiohttp import AiohttpSession
# http://proxy.server:3128/
bot = Bot("5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher()

@dp.message(CommandStart())
async def signup(message: types.Message, state: FSMContext):
    await database(message.from_user.id)
    await message.answer(f"Salom <b>{message.from_user.full_name}</b>\ntugmalardan birini tanlang", parse_mode='HTML', reply_markup=menus_button)

@dp.message()
async def Menus(message: types.Message, state: FSMContext):
    if message.text == "Tarjimon":
        await state.set_state(Translate.lang)

@dp.message(Translate.lang)
async def TranslateLang(message: types.Message, state: FSMContext):
    await state.update_data(lang=message.text)
    await message.answer("tarjima qilmoqchi bo'lgan matningizni kiriting")
    await state.set_state(Translate.trans)

@dp.message(Translate.trans)
async def translate(message: types.Message, state: FSMContext):
    data1 = await state.get_data()
    if data1.get("lang") == "🇺🇿 O'zbekcha - English 🇺🇸":
        text = GoogleTranslator(source='uz', target='en').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇸 English - O'zbekcha 🇺🇿":
        text = GoogleTranslator(source='en', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Русский 🇷🇺":
        text = GoogleTranslator(source='uz', target='ru').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇷🇺 Русский - O'zbekcha 🇺🇿":
        text = GoogleTranslator(source='ru', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "bilmayman":
        text = GoogleTranslator(source='auto', target='')
    await state.set_state(Translate.lang)

@dp.startup()
async def startup(bot: Bot):
    try:
        await bot.send_message(chat_id=5230484991, text="Bot ishga tushdi❗")
    except:
        pass

@dp.shutdown()
async def shutdown(bot: Bot):
    try:
        await bot.send_message(chat_id=5230484991, text="Bot to'xtadi❗")
    except:
        pass

async def start():
    # session = AiohttpSession(proxy="http://proxy.server:3128/")
    # , session=session
    await bot.set_my_commands([
        types.BotCommand(command='/start', description="botni ishga tushurish")
    ])
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
run(start())