from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

languages_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbekcha - English 🇺🇸"), KeyboardButton(text="🇺🇸 English - O'zbekcha 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Русский 🇷🇺"), KeyboardButton(text="🇷🇺 Русский - O'zbekcha 🇺🇿")],
    ],
    resize_keyboard=True
)

menus_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tarjimon"), KeyboardButton(text=" Video yuklash")],
        [KeyboardButton(text="Ob havo malumotlari")],
        [KeyboardButton(text="rasm fonini olib tashlang")],
        [KeyboardButton(text="wikipedia")],
    ]
)

async def database(id):
    with open('database.txt', 'r') as file:
        read = file.read()
        if str(id) not in read:
            with open('database.txt', 'a') as file:
                file.write(f" {id} ")
        else:
            pass