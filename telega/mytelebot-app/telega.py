import telebot
import const
import time
import main as n
import mat as m

from time import gmtime, strftime

bot = telebot.TeleBot(const.token)

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = 100)
markup.row('Привет', 'Пока', 'Время ⌚')

@bot.message_handler(commands=['start'])

def first(message):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.row('Начать')
    send = bot.send_message(message.from_user.id, 'Давай посмотрим какие доступны команды:', reply_markup = key)
    bot.register_next_step_handler(send, second)

def second(message):
    if message.text == 'Начать':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 1', 'Время ⌚','Погода ⛅', 'Назад ↩')
        send = bot.send_message(message.from_user.id, "Второй подуровень", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    else:
        send_text(message)

def third(message):
    if message.text == 'Кнопка 1':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 2', 'Кнопка 3', 'Назад ↩', 'Главная')
        send = bot.send_message(message.from_user.id, "Третий подуровень", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)

    elif message.text == 'Время ⌚':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 1', 'Время ⌚', 'Погода ⛅','Главная')
        send = bot.send_message(message.from_user.id, 'Текущая дата и Время:', reply_markup=keyboard)
        bot.send_message(message.chat.id, strftime("%A, %d %B %Y %H:%M:%S"))
        bot.register_next_step_handler(send, third)

    elif message.text == 'Погода ⛅':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Алматы', 'Санкт-Петербург','Назад ↩')
        send = bot.send_message(message.from_user.id, 'Выберите город:', reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)
        # bot.send_message(message.from_user.id, 'Максимальная температура: {0}\nМинимальная температура: {1}\n\nОписание:{2}'.format(n.t_max,n.t_min,n.text))

    elif message.text == 'Назад ↩':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 1', 'Время ⌚','Погода ⛅','Главная')
        send = bot.send_message(message.from_user.id, "Второй подуровень", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == 'Главная':
        first(message)
    else:
        send_text(message)

def fourth(message):
    if message.text == 'Алматы':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        n.weather1()
        send = bot.send_message(message.from_user.id,'Погода в Алматы сегодня:\n\n🌡 Текущая температура составляет: {0}\n\n☀ Возможная максимальная температура:{1}\n❄ Возможная минимальная температура:{2}\n\n💭 Описание:{3}'.format(n.t_now,n.t_max,n.t_min,n.text),reply_markup=keyboard)
        keyboard.row('Назад ↩')
        bot.register_next_step_handler(send, fourth)
    elif message.text == 'Санкт-Петербург':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        n.weather2()
        send = bot.send_message(message.from_user.id,'Погода в Санкт-Петербурге сегодня:\n\n🌡 Текущая температура составляет: {0}\n\n☀ Возможная максимальная температура:{1}\n❄ Возможная минимальная температура:{2}\n\n💭 Описание:{3}'.format(n.t_now,n.t_max,n.t_min,n.text),reply_markup=keyboard)
        keyboard.row('Назад ↩')
        bot.register_next_step_handler(send, fourth)

    elif message.text == 'Кнопка 2':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 2', 'Кнопка 3', 'Назад ↩', 'Главная')
        send = bot.send_message(message.from_user.id, "Кнопка 2 АКТИВНА", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == 'Кнопка 3':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 2', 'Кнопка 3', 'Назад', 'Главная')
        send = bot.send_message(message.from_user.id, "Кнопка 3 АКТИВНА", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == 'Назад ↩':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 1', 'Время ⌚', 'Погода ⛅', 'Главная')
        send = bot.send_message(message.from_user.id, "Второй подуровень", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == 'Главная':
        first(message)
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Кнопка 7', 'Назад на 2 уровень','Главная')
        send = bot.send_message(message.from_user.id, 'Уровень 3', reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id,'Добрый день {0} {1}!'.format(message.from_user.last_name,message.from_user.first_name))
    elif message.text == 'Время ⌚':
        bot.send_message(message.chat.id, strftime("%A, %d %B %Y %H:%M:%S"))
    elif message.text == 'Пока':
        bot.send_message(message.chat.id,'Надеюсь еще увидимся {0} {1}!'.format(message.from_user.last_name,message.from_user.first_name))

    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIP915-ORlnNt87N9EwxUibo16-MkdTAAJmCQACeVziCZ8KivlhthhEGAQ')
    elif message.text.lower() == 'лиза':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIQA15-OtouzehwyvZmmu_amjppJDR2AAJSCQACeVziCanLMz1x9P1tGAQ')
    elif message.text.lower() == 'алан':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIQAV5-Or_SFDaO-uJNrBYYu17O_AF6AAJkCQACeVziCVPcx3du2nzHGAQ')
    elif message.text.lower() == 'ислам':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBz15-Qf2AKy751--HS_ECNU8u3Pt8AAICAQACFnxoAwgzPloel5AcGAQ')


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    print(message)

bot.polling()
