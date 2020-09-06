from flask import Flask, redirect, url_for, request, render_template
import requests
from requests import get
from bs4 import BeautifulSoup
import random
import datetime
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import json




app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/<firstName>/')
def homepage2(firstName):
    url = 'https://www.oberlo.com/blog/motivational-quotes'
    response = get(url)
    html_Soup = BeautifulSoup(response.text, 'html.parser')
    quoteList = []

    for child in html_Soup.body.find_all('span'):
        quoteList.append(str(child.string))

    newList = []
    for x in range(0, len(quoteList)):
        if quoteList[x].find('“') == 0 and len(quoteList[x]) > 2:
            newList.append(quoteList[x])
    generatedQuote = newList[random.randint(0, len(newList))]
    currentTime = grabHour()
    numericalDate, weekDay = grabDate()
    condition, userCity, hiTemp, lowTemp = grabWeather()

    return render_template('homePage2.html', name = firstName, quote = generatedQuote, time = currentTime,
                           date = numericalDate, dayOfWeek = weekDay, weather = condition, city = userCity,
                           hi = hiTemp, low = lowTemp)

@app.route('/<firstName>/<lastName>/')
def homePage(firstName, lastName):
    url = 'https://www.oberlo.com/blog/motivational-quotes'
    response = get(url)
    html_Soup = BeautifulSoup(response.text, 'html.parser')
    quoteList = []

    for child in html_Soup.body.find_all('span'):
        quoteList.append(str(child.string))

    newList = []
    for x in range(0, len(quoteList)):
        if quoteList[x].find('“') == 0 and len(quoteList[x]) > 2:
            newList.append(quoteList[x])
    generatedQuote = newList[random.randint(0, len(newList))]

    # Here we are getting the time from our grabHour method
    currentTime = grabHour()
    numericalDate, weekDay = grabDate()
    condition, userCity, hiTemp, lowTemp = grabWeather()

    return render_template('homePage.html', name = firstName, name2 = lastName, quote = generatedQuote,
                           time = currentTime, date = numericalDate, dayOfWeek = weekDay, weather = condition,
                            city = userCity, hi = hiTemp, low = lowTemp)


def grabHour():
    currentTimeRaw = datetime.datetime.today()
    hourSimple = currentTimeRaw.strftime("%H:%M")
    if(datetime.datetime.today().hour > 12):
        hour = currentTimeRaw.hour - 12
        return str(hour) + currentTimeRaw.strftime(":%M")
    else:
        return hourSimple

def grabDate():
    currentTimeRaw = datetime.datetime.today()
    dateNum = currentTimeRaw.strftime("%x")
    weekDay = currentTimeRaw.strftime("%A")
    return dateNum, weekDay

def grabLocation():
    ipData = 'http://api.ipstack.com/check?access_key=abcdefg'
    r = requests.get(ipData)
    j = json.loads(r.text)
    lat = j['latitude']
    long = j['longitude']
    city = j['city']
    return lat, long, city

def grabWeather():
    data = YahooWeather(APP_ID="abcdefg",
                        api_key="abcdefg",
                        api_secret="abcdefg")

    userLat, userLong, userCity = grabLocation()

    data.get_yahoo_weather_by_location(userLat, userLong, Unit.fahrenheit)

    condition = data.condition.text
    high = data.forecasts[0].high
    low = data.forecasts[0].low


    return condition, userCity, high, low

if __name__ == "__main__":
    app.debug = True
    app.run()
