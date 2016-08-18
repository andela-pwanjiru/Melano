import os
import requests
from django.shortcuts import render

# Create your views here.
API_KEY = os.environ.get('API_KEY')

# API_KEY = '1f69d4da3a4679a2fc00ce09a09a93e7'

def get_city_weather(request):
    if request.method == "POST":
        city = request.POST.get('city')
        # payload = {'APPID': API_KEY, 'q': city, 'units': 'metric'}
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?'+'APPID=' + API_KEY + '&q=' + city)
        # r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
        # import pdb ; pdb.set_trace()
        y = r.json()
        weather = y['weather'][0]['main']
        weather_icon = y['weather'][0]['icon']
        wind = y['wind']['speed']
        return render(request, "api.html", {'weather': weather, 'weather_icon':  weather_icon, 'windspeed': wind })
    else:
        return render(request, 'api.html')
