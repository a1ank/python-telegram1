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
