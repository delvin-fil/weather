#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import urllib, math, json, time, re, warnings,  requests, datetime, ephem
from bs4 import BeautifulSoup
from pprint import pprint
import urllib.request
from datetime import date
from math import radians as rad,degrees as deg 


warnings.filterwarnings("ignore")
localtime = time.localtime(time.time())
z = str(localtime[3])
y = str(localtime[4])

cmd = 'sensorsNearby'
uuid = 'UUID_narodmon'
api_key = 'YOU_API_KEY_narodmon'
radius = '11'
lat = '54.643600' # Ваши координаты
lng = '86.198808' # Ваши координаты
lang = 'ru'
radius = '30'
types = '1,2' 

#http://maps.googleapis.com/maps/api/elevation/xml?locations=86.198808,54.643600&sensor=true
headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                  'Firefox/14.0.1'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}

WeHtml = requests.get('http://narodmon.ru/api/sensorsNearby?lat=' + lat + '&lng=' + lng + '&radius=' + radius + '&uuid=' + uuid + '&api_key=' + api_key + '&lang=' + lang, headers=headers).text
soup = BeautifulSoup(WeHtml)
soup = str(soup)
soup = re.sub(r'\<[^>]*\>', '', soup)
fact = json.loads(soup)
temp1 = fact['devices'][0]['sensors'][0]['value']
temp2 = fact['devices'][1]['sensors'][0]['value']
#davl = str(round(fact['devices'][0]['sensors'][1]['value']))
#a = fact['devices'][0]['location']
sredn = str(round(((temp1) + temp2) / 2))
#print ("${color cyan}${font ubuntu:size=11}${alignr 75}${voffset -25}" + davl + ' мм.р.c.')
#print ("${color cyan}${font ubuntu:size=11}${alignr 85}${voffset -28}" + a)


obs = ephem.Observer()
sun = ephem.Sun()
obs.lat = "54.6436"
obs.long = "86.1988"
obs.date = datetime.datetime.today()
rise_time = obs.next_rising(sun)
set_time = obs.next_setting(sun)
sunrise = ephem.localtime(rise_time).strftime('%H:%M')
sunset = ephem.localtime(set_time).strftime('%H:%M')
moon = ephem.Moon()
m_rise_time = obs.next_rising(moon)
m_set_time = obs.next_setting(moon)
moonrise = ephem.localtime(m_rise_time).strftime('%H:%M')
moonset = ephem.localtime(m_set_time).strftime('%H:%M')

g = ephem.Observer()  
g.name='Somewhere'  
g.lat=rad(54.6436)  # lat/long in decimal degrees  
g.long=rad(86.1988)  
  
m = ephem.Moon()  
  
g.date = date.today()# local time zone, I'm in UTC+1  
g.date -= ephem.hour # always everything in UTC  
#print (g.date, ephem.localtime(g.date).time().strftime("%H%M"))  
for i in range(1): # compute position for every 15 minutes  
    m.compute(g)  
  
    nnm = ephem.next_new_moon(g.date)  
    pnm = ephem.previous_new_moon(g.date)  
    # for use w. moon_phases.ttf A -> just past  newmoon,  
    # Z just before newmoon  
    # '0' is full, '1' is new  
    # note that we cannot use m.phase as this is the percentage of the moon  
    # that is illuminated which is not the same as the phase!  
    lunation=(g.date-pnm)/(nnm-pnm)  
    symbol=lunation*26 
     
    if symbol < 0.2 or symbol > 25.8 :  
        symbol = '1'  # new moon  
    else:  
        symbol = chr(ord('a')+int(symbol+0.5)-1)  
  
    #print(ephem.localtime(g.date).time(), deg(m.alt),deg(m.az), ephem.localtime(g.date).time().strftime("%H%M"),  m.phase,symbol)
    mp = str(round(m.phase)) + "%"
    print("${color #AAAAAA}${font Moon\ Phases:size=24:bold}${offset 70}${voffset -12}" + symbol, "${font Ubuntu:size=16:bold}${offset -30}${voffset -10}" + mp)  
    g.date += ephem.minute*15

if int(sredn) > 0:
    sredn = "+"+str(sredn)

print ("${color red}${font zekton:size=24:bold}${offset 80}${voffset 0}" + sredn + '°')
print ("${color yellow}${voffset -85}${font Ubuntu:size=11}Восход${alignr}${color cyan}Закат")
print ("${voffset -3}${color yellow}" + sunrise + "${alignr}${color cyan}" + sunset)
print ("${color aaaaaa}${voffset -3}Луна${alignr}Луна")
print ("${voffset -3}" + moonrise + "${alignr}" + moonset)
