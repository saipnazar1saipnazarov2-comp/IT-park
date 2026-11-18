
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Janggovor"), KeyboardButton(text="Ramantik")],
        [KeyboardButton(text="Serial"), KeyboardButton(text="Ujis")]
    ],
    resize_keyboard=True
)

jang_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Alfa"), KeyboardButton(text="Qasoskorlar")],
        [KeyboardButton(text="JonUki"), KeyboardButton(text="Transformerlar")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

qasos_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Qasoskorlar-1"), KeyboardButton(text="Qasoskorlar-2")],
        [KeyboardButton(text="Qasoskorlar-3"), KeyboardButton(text="Qasoskorlar-4")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

transformer_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Transformerlar 1")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

jonuki_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="JonUki 1"),
         KeyboardButton(text="JonUki 2")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)


































