import const
import telebot
import random

from telebot import types

bot = telebot.TeleBot(const.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1,item2)

    bot.send_message(message.chat.id, 'Welcome,{0.first_name}!\nЯ - </b>{1.first_name}</b>, THIS IS A NEW BOT.'.format(message.from_user,bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id,message.text)

bot.polling(none_stop=True)
