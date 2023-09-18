import time
import requests
from bs4 import BeautifulSoup
from plyer import notification


def getData(url):
    r = requests.get(url)
    return r.text


htmlData = getData("https://weather.com/en-IN/weather/today/l/b49ee5a8038f8500ac3bdb52f878f5984c4fd92ad290180ed5fe3ef7d5a2ea5f")

soup = BeautifulSoup(htmlData, 'html.parser')

current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

current_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = str(current_temp)
temp_rain = str(current_rain)

result = notification.notify(title = 'Liver Weather update', message = f'current_temp {temp[123:-9]} in rewa, Madhya Pradesh\n{temp_rain[131:-14]}', timeout = 2)

time.sleep(5)
# result = "current_temp " + temp[128:-9] + "  in patna bihar" + "\n" + temp_rain[131:-14]
# n.show_toast("live Weather update", 
#             result, duration = 10)
