from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup


def Start_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('search'))
    return markup


def Shakarlar():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('ташкент'),
        KeyboardButton('сырдарья'),
        KeyboardButton('бухара'),
        KeyboardButton('самарканд'),
        KeyboardButton('ургенч'),
        KeyboardButton('нукус'),
        KeyboardButton('джизак'),
        KeyboardButton('наманган'),
        KeyboardButton('фергана'),
        KeyboardButton('карши'),
        KeyboardButton('гулистан'),
        KeyboardButton('андижан')

    )
    return markup