import telebot
import const
import time
import main as n

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
    print('первый')

def second(message):
    if message.text == 'Начать':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Covid-19', 'Время ⌚','Погода ⛅', 'Назад ↩')
        send = bot.send_message(message.from_user.id, "Второй подуровень", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
        print('второй')
    else:
        send_text(message)

def third(message):
    if message.text == 'Covid-19':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Covid-19', 'Время ⌚', 'Погода ⛅','Назад ↩')
        n.corona()
        send = bot.send_message(message.from_user.id,'📊 Текущая статистика о коронавирусе {0}\n\n😷 Заражено: {1}\n😌 Выздоровело: {2}\n☠️ Умерло: {3}'.format(n.t_now[12:26],n.t_now[26:31],n.t_now[40:44],n.t_now[66:69]), reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
        print('третий')

    elif message.text == 'Время ⌚':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Covid-19', 'Время ⌚', 'Погода ⛅','Назад ↩')
        send = bot.send_message(message.from_user.id, 'Текущая дата и Время: \n{0}'.format(strftime("%A, %d %B %Y %H:%M:%S")), reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
        print('третий')

    elif message.text == 'Погода ⛅':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Алматы', 'Санкт-Петербург','Назад ↩')
        send = bot.send_message(message.from_user.id, 'Выберите город или напишите название города:', reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)
        print('третий')

    elif message.text == 'Назад ↩':
        first(message)
    else:
        send_text(message)

def fourth(message):
        if message.text == 'Алматы':
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            n.weather1()
            send = bot.send_message(message.from_user.id,'Погода в Алматы сегодня:\n\n🌡 Текущая температура составляет: {0}\n\n☀ Возможная максимальная температура:{1}\n❄ Возможная минимальная температура:{2}\n\n💭 Краткое описание:\n{3}'.format(n.t_now,n.t_max[5:10],n.t_min[4:9],n.text),reply_markup=keyboard)
            keyboard.row('Назад ↩')
            bot.register_next_step_handler(send, fourth)
            print('четвёртый')

        elif message.text == 'Санкт-Петербург':
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            n.weather2()
            send = bot.send_message(message.from_user.id,'Погода в Санкт-Петербурге сегодня:\n\n🌡 Текущая температура составляет: {0}\n\n☀ Возможная максимальная температура:{1}\n❄ Возможная минимальная температура:{2}\n\n💭 Краткое описание:\n{3}'.format(n.t_now,n.t_max[5:10],n.t_min[4:9],n.text),reply_markup=keyboard)
            keyboard.row('Назад ↩')
            bot.register_next_step_handler(send, fourth)
            print('четвёртый')

        elif message.text == 'Назад ↩':
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            keyboard.row('Covid-19', 'Время ⌚', 'Погода ⛅', 'Назад ↩')
            send = bot.send_message(message.from_user.id, "Второй подуровень", reply_markup=keyboard)
            bot.register_next_step_handler(send, third)
            print('четвёртый')

        elif message.text == 'Главная':
            first(message)

        else:
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            n.weather3(message.text)
            try:
                send = bot.send_message(message.from_user.id,
                'Погода в городе {0} на сегодня:\n\n🌡 Текущая температура составляет: {1}\n\n☀ Возможная максимальная температура:{2}\n❄ Возможная минимальная температура:{3}\n\n💭 Краткое описание:\n{4}'.format(message.text,n.t_now,n.t_max[5:10],n.t_min[4:9],n.text),reply_markup=keyboard)
                keyboard.row('Назад ↩')
                bot.register_next_step_handler(send, fourth)
                print('try')
            except:
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
                n.weather3(message.text)
                send = bot.send_message(message.from_user.id,
                'К сожалению такого города не существует. Проверьте правильность написания.',reply_markup=keyboard)
                keyboard.row('Назад ↩')
                bot.register_next_step_handler(send, fourth)
                print('except')



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
