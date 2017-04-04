import requests
import urllib.request
from xml.dom.minidom import parseString
from datetime import datetime
cur_hour = int(datetime.strftime(datetime.now(), "%H"))
headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                  'Firefox/14.0.1'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}

win = requests.get('http://api.pogoda.com/index.php?api_lang=ru&localidad=237263&affiliate_id=YOU_API_KEY_pogoda.ru&v=2&h=1', headers=headers).text
wint  = parseString(win)
win = wint.getElementsByTagName('day')[0]
w = win.getElementsByTagName('wind')[cur_hour]

w = w.attributes['value'].value
#print (w)
if w == "1":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый северный")
elif w == "2":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Северо-восточный")
elif w == "3":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Восточный")
elif w == "4":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Юго-восточный")
elif w == "5":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Южный")
elif w == "6":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Юго-западный")
elif w == "7":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Западный")
elif w == "8":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Слабый Северо-западный")
elif w == "9":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный северный")
elif w == "10":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Северо-восточный")
elif w == "11":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Восточный")
elif w == "12":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Юго-восточный")
elif w == "13":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Южный")
elif w == "14":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Юго-западный")
elif w == "15":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Западный")
elif w == "16":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Умеренный Северо-западный")
elif w == "17":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный северный")
elif w == "18":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Северо-восточный")
elif w == "19":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Восточный")
elif w == "20":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Юго-восточный")
elif w == "21":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Южный")
elif w == "22":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Юго-западный")
elif w == "23":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Западный")
elif w == "24":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Сильный Северо-западный")
elif w == "25":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный северный")
elif w == "26":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Северо-восточный")
elif w == "27":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Восточный")
elif w == "28":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Юго-восточный")
elif w == "29":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Южный")
elif w == "30":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Юго-западный")
elif w == "31":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Западный")
elif w == "32":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ураганный Северо-западный")
elif w == "33":
	print("${voffset -3}${font ubuntu:size=11}${color cyan}${alignc}Ветер с переменным направлением")
