#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import urllib.request
#f = urllib.request.urlopen('http://gismeteo.ru')
#print(f.read(300))
import lxml.html
import requests, re, time, subprocess
import urllib.request
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("always")

localtime = time.localtime(time.time())

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                  'Firefox/14.0.1'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}

#page = requests.get('http://informer.gismeteo.ru/xml/22113.xml', headers=headers).text
page = requests.get('http://informer.gismeteo.ru/xml/99845.xml', headers=headers).text
xmldoc = parseString(page)
town = xmldoc.getElementsByTagName('TOWN')
townm = town[0].attributes['sname'].value
#townm = townm.decode('utf-8').encode('cp1251')
#print (townm)
forecast = xmldoc.getElementsByTagName('FORECAST')			# информация о сроке
temperature = xmldoc.getElementsByTagName('TEMPERATURE')	# температура
phenomena = xmldoc.getElementsByTagName('PHENOMENA')	# атмосферные явления
pressure = xmldoc.getElementsByTagName('PRESSURE')		# давление
wind = xmldoc.getElementsByTagName('WIND')			# ветер
relwet = xmldoc.getElementsByTagName('RELWET')		# влажность
hour1 = int(forecast[0].attributes['hour'].value)
tempers = int(temperature[0].attributes['max'].value) + int(temperature[0].attributes['min'].value) / 2
tempers = round(tempers)
if tempers > 0:
	tempers = '+' + str(tempers)
print ("${font Magistral:size=16:bold}${color red}${offset 10}", '{}°'.format(tempers), "${font ubuntu:size=11}")
print (("${voffset -3}${color cyan}"), ('{}:00'.format(hour1)), ("${color ffff00}"))
phen = phenomena[0].attributes['cloudiness'].value

if localtime[3] > 9:
	path = "/home/fil/conky/day/"
if localtime[3] > 21:
	path = "/home/fil/conky/night/"
if localtime[3] < 9:
	path = "/home/fil/conky/night/"

if phen == "0":
	print ("${voffset -3}Ясно")
	print ("${voffset -15}${image " + path + "sunny.png -p 70,710 -s 38x38 }")
elif phen == "1":
	print ("${voffset -3}Малооблачно")
	print ("${voffset -15}${image " + path + "sunny-1.png -p 70,710 -s 38x38 }")
elif phen == "2":
	print ("${voffset -3}Облачно")
	print ("${voffset -15}${image " + path + "sunny-2.png -p 70,710 -s 38x38 }")
elif phen == "3":
	print ("${voffset -3}Пасмурно")
	print ("${voffset -15}${image " + path + "overcast.png -p 70,710 -s 38x38 }")
prec = phenomena[0].attributes['precipitation'].value
if prec == "4":
	print ("${voffset -3}Дождь")
	print ("${voffset -15}${image " + path + "rain.png -p 70,710 -s 38x38 }")
elif prec == "5":
	print ("${voffset -3}Ливень")
	print ("${voffset -15}${image " + path + "rain-2.png -p 70,710 -s 38x38 }")
elif prec == "6":
	print ("${voffset -3}Снег")
	print ("${voffset -15}${image " + path + "snow.png -p 70,710 -s 38x38 }")
elif prec == "7":
	print ("${voffset -3}Снег")
	print ("${voffset -15}${image " + path + "sunny-1.png -p 70,710 -s 38x38 }")
elif prec == "8":
	print ("${voffset -3}Гроза")
	print ("${voffset -15}${image " + path + "flash.png -p 70,710 -s 38x38 }")
elif prec == "9":
	print ("${voffset -3}Нет данных")
	#print ("${voffset -15}${image " + path + "vopr.png -p 70,710 -s 38x38 }")
elif prec == "10":
	print ("${voffset -3}Без осадков")
	#print ("${voffset -15}${image " + path + "sunny.png -p 70,710 -s 38x38 }")


print ("${voffset -3}Давл.: "+pressure[0].attributes['max'].value+" м.р.с")
print ("${voffset -3}Ветер: "+wind[0].attributes['max'].value+" м.с.")
#-------------------------
wind1 = wind[0].attributes['direction'].value
if wind1 == "0":
	print ("${voffset -3}Северный")
elif wind1 == "1":
	print ("${voffset -3}Северо-восточный")
elif wind1 == "2":
	print ("${voffset -3}Восточный")
elif wind1 == "3":
	print ("${voffset -3}Юго-восточный")
elif wind1 == "4":
	print ("${voffset -3}Южный")
elif wind1 == "5":
	print ("${voffset -3}Юго-западный")
elif wind1 == "6":
	print ("${voffset -3}Западный")
elif wind1 == "7":
	print ("${voffset -3}Северо-западный")
tmpmax = int(temperature[3].attributes['max'].value)
if tmpmax > 0:
	tmpmax = '+' + str(tmpmax)
tmpmin = int(temperature[3].attributes['min'].value)
if tmpmin > 0:
	tmpmin = '+' + str(tmpmin)

print ("${voffset -3}${color FF5C00}Завтра: ",'{}° {}°'.format(tmpmin, tmpmax))
phen1 = phenomena[3].attributes['cloudiness'].value
if phen1 == "0":
	print ("${voffset -3}Ясно")
elif phen1 == "1":
	print ("${voffset -3}Малооблачно")
elif phen1 == "2":
	print ("${voffset -3}Облачно")
elif phen1 == "3":
	print ("${voffset -3}Пасмурно")
#-------------------------------------------------------------
'''#html_doc = ('http://beta.gismeteo.ru/weather-leninsk-kuznetsky-11835/')
html_doc = ('https://www.gismeteo.ru/city/daily/11835/')
WeHtml = urllib.request.urlopen(html_doc)
soup = BeautifulSoup(WeHtml)
word = soup.find('div', 'icon')
#print (word)
word = soup.find('dt', 'png')
word = str(word)
#print (word)
if localtime[3] <= 9 and localtime[3] >= 21:
	word1 = (word[87:99])
else:
	word1 = (word[87:98])
uri = (word[47:87])
#print (uri,'ХУЙ\n')
#word1 = (word[87:99])

word1 = word1.replace('t', '')
word1 = word1.replace('i', '')
word1 = word1.replace('l', '')
word1 = word1.replace('g', '')
word1 = word1.replace('p', '')
word1 = word1.replace('e', '')
word1 = word1.replace(')', '')
word1 = word1.replace('"', '')
#word1 = ' '.join(word1.split())
#print (word)
IcoUrl = (
    'http://' + uri +
    word1 +
    'png')
#print (IcoUrl, '\n', '\n', '\n', '\n', '\n', '\n')
#IcoUrl = (
#    'http://bbst4.gismeteo.ru/assets/flat-ui/img/icons/weather/flat/svg/' 
#    'https://st6.gismeteo.ru/static/images/icons/new/' +
#    word1 +
#    '.png')
#print (IcoUrl)
IcoHtml = urllib.request.urlopen(IcoUrl)
IcoPage = IcoHtml.read()
fh = open('/home/fil/icon.png', 'wb')
fh.write(IcoPage)
fh.close()
print ("${image /home/fil/icon.gif -p 70,710 -s 38x38 }")


### ПЕРЕИМЕНОВАТЬ КАРТИНКИ В КАТАЛОГЕ CONKY И ДОБАВИТЬ К БЛОКУ direction'''
#subprocess.Popen("pwd", stderr=None, shell=True)