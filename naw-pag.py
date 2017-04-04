#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import requests, re, time, subprocess, sys
from datetime import datetime
import urllib.request
from xml.dom.minidom import parseString
import warnings

start = time.clock()
warnings.filterwarnings("ignore")
localtime = time.localtime(time.time())

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                   'Firefox/14.0.1'),
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':
    'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':
    'gzip, deflate',
    'Connection':
    'keep-alive',
    'DNT':
    '1'
}

path = '/home/fil/codding/pogoda/icons/tiempo-weather/galeria5/'
bar = requests.get(
    'http://api.pogoda.com/index.php?api_lang=ru&localidad=237263&affiliate_id=4h5o9wy3uyjp&v=2&h=1',
    headers=headers).text
bardoc = parseString(bar)
#--------------------ТЕМПЕРАТУРА
cur_hour = int(datetime.strftime(datetime.now(), "%H"))
day = bardoc.getElementsByTagName('day')[0]
tmn = day.getElementsByTagName('tempmin')[0]
tmx = day.getElementsByTagName('tempmax')[0]
tempmin = int(tmn.attributes['value'].value)
tempmax = int(tmx.attributes['value'].value)
if tempmax > 0:
    tempmax = "+" + str(tempmax)

if tempmin >= 0:
    tempmin = "+" + str(tempmin)
tempmin = str(tempmin)
tempmax = str(tempmax)

#-------------------ПОГОДА
s = day.getElementsByTagName('symbol')[cur_hour]
symbol = s.attributes['desc'].value
icons = s.attributes['value'].value
#------------------------------------------------------------------

#-------------------ДАВЛЕНИЕ

pres = day.getElementsByTagName('pressure')[cur_hour]
pressure = int(pres.attributes['value'].value)
pressure = round(pressure * 0.750063)

#------- ЗАВТРА/ПОСЛЕЗАВТРА
tmnz = bardoc.getElementsByTagName('day')[1]
tmnz = tmnz.getElementsByTagName('tempmin')[0]
tmxz = bardoc.getElementsByTagName('day')[1]
tmxz = tmxz.getElementsByTagName('tempmax')[0]
tempminz = int(tmnz.attributes['value'].value)
tempmaxz = int(tmxz.attributes['value'].value)
tempz = round((tempminz + tempmaxz) / 2)
if tempz > 0:
    tempz = "+" + str(tempz)
tempz = str(tempz)
sz = bardoc.getElementsByTagName('day')[1]
sz = sz.getElementsByTagName('symbol')[0]
iconsz = sz.attributes['value'].value

tmnpz = bardoc.getElementsByTagName('tempmin')[2]
tmxpz = bardoc.getElementsByTagName('tempmax')[2]
tempminpz = int(tmnpz.attributes['value'].value)
tempmaxpz = int(tmxpz.attributes['value'].value)
temppz = round((tempminpz + tempmaxpz) / 2)
if temppz > 0:
    temppz = "+" + str(temppz)
temppz = str(temppz)
spz = bardoc.getElementsByTagName('day')[2]
spz = spz.getElementsByTagName('symbol')[0]
iconspz = spz.attributes['value'].value
#------------------------------------------------------------------
vat = requests.get(
    'http://api.pogoda.com/index.php?api_lang=ru&localidad=237263&affiliate_id=4h5o9wy3uyjp',
    headers=headers).text
xmld = parseString(vat)
veter0 = xmld.getElementsByTagName('forecast')[14]  # ветер
veter = str(veter0.attributes['value'].value)  # ветер
#------------------------------------------------------------------
print(
    "${voffset 10}${font ubuntu:size=11}${color cccccc}Температура: ${font zekton:size=10:bold}${alignr}${color 9999FF}"
    + tempmin + "   ${color FF9999}" + tempmax + "${color cccccc} °C${font}")
print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}", symbol)
#import wind
print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}", veter)
print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc} Давление: ",
      pressure, "мм.р.с")
print(
    "${voffset -3}${font ubuntu:size=13}${color 00ff00}Завтра${alignr}Послезавтра"
)
print("${voffset 0}${color yellow}${font zekton:size=12:bold}${voffset -3}",
      tempz, "°C${alignr 5}${voffset 0}", temppz, "°C")
print("${image " + path + icons + '.png' + " -p 60,745 -s 80x80 -f 1800}")
print("${image " + path + iconsz + '.png' + " -p 0,770 -s 50x50 -f 1800}")
print("${image " + path + iconspz + '.png' + " -p 150,770 -s 50x50 -f 1800}")
#------------------------------------------------------------------
finish = time.clock()
itog = str(round(finish - start, 3))
import mon2

#print(itog+" sec.")
