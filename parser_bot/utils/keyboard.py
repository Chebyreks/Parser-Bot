from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Посмотреть лучшее предложение за сегодня'),
            KeyboardButton(text='Посмотреть статистику')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбери действие'
)

return_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вернуться'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбери действие'
)

hello_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Здаровчик'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбери действие'
)

confirm_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбери действие'
)