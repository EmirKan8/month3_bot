from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)
    quiestion = "В каком году был основан Geeks?"
    answers = ['2005', '2010', '2018', 'Я не знаю']


    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )
async def quiz_3(callback: types.CallbackQuery):

        markup = InlineKeyboardMarkup()
        next_button = InlineKeyboardButton("NEXT", callback_data="next_button_3")
        markup.add(next_button)
        quiestion = "Какого числа Нооруз? "
        answers = ['18',
                   '20',
                   '11',
                   '21']

        await callback.message.answer_poll(
            question=quiestion,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,

        )
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")

