import telebot
import requests
from bs4 import BeautifulSoup as BS


def weather1():
    global t_now

    try:
        r = requests.get('https://tengrinews.kz')
        html = BS(r.content, 'html.parser')

        for el in html.select('.my-app'):
            t_now = el.select('.tn-urgent-news-message')[0].text
            print('Текущая статистика о коронавирусе {0}\n\nПодтвержденных случаев заражения:{1}\nПодтвержденных случаев выздоровления: {2}\nПодтвержденных случаев смертей:{3}'.format(t_now[12:25],t_now[26:30],t_now[40:44],t_now[65:68]))
    except:
        print('Ошибка')





print(weather1())
