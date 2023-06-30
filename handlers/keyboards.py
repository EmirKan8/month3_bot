from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
dice_button = KeyboardButton("/dice")
reg_button = KeyboardButton("/reg")
start_markup.add(
    start_button,
    quiz_button,
    mem_button,
    dice_button,
    reg_button
)

cancel_button = KeyboardButton("cancel")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    cancel_button
)




submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("да"),
    KeyboardButton("заново"),
    cancel_button
)