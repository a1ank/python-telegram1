import telebot
import requests
from bs4 import BeautifulSoup as BS


def weather1():
    global t_now
    global t_min
    global t_max
    global text

    r = requests.get('https://sinoptik.ua/погода-алматы')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_now = el.select('.imgBlock .today-temp')[0].text
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

def weather2():
    global t_now
    global t_min
    global t_max
    global text

    r = requests.get('https://sinoptik.ua/погода-санкт-петербург')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_now = el.select('.imgBlock .today-temp')[0].text
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

def weather3(city):
    global t_now
    global t_min
    global t_max
    global text
    t_now = 0
    t_min = 0
    t_max = 0
    text = 0



    h = 'https://sinoptik.ua/погода-'+ city
    r = requests.get(h)
    html = BS(r.content, 'html.parser')
    for el in html.select('#content'):
        t_now = el.select('.imgBlock .today-temp')[0].text
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text



def corona():
    global t_now

    r = requests.get('https://tengrinews.kz/tag/Коронавирус-в-Казахстане')
    html = BS(r.content, 'html.parser')

    for el in html.select('.my-app'):
        t_now = el.select('.tn-urgent-news-message')[0].text
