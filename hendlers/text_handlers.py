import requests
from bs4 import BeautifulSoup as BS
from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from keboards import *



@bot.message_handler(func=lambda message: message.text == 'search')
def reaction_shaxarlar(message: Message):
    chat_id = message.chat.id
    svg = bot.send_message(chat_id, 'shahar nomi', reply_markup=Shakarlar())
    bot.register_next_step_handler(svg, Ob_havo)


def Ob_havo(messsage: Message):
    chat_id = messsage.chat.id
    t = requests.get(f'https://sinoptik.ua/погода-{messsage.text.title()}')
    html_t = BS(t.content, 'html.parser')

    for el in html_t.select('#content'):
        min = el.select('.temperature .min')[0].text
        max = el.select('.temperature .max')[0].text
        t_min = min[4:]
        t_max = max[5:]
        bot.send_message(chat_id,f"Harorat Min:  {t_min} Max: {t_max}")
