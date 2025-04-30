
# Create your views here.
from django.shortcuts import render
from .forms import CityForm
from .utils import get_weather_data
import requests
def home(request):
    weather = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = get_weather_data(city)
    else:
        form = CityForm()
    return render(request, 'home.html', {'form': form, 'weather': weather})

def get_weather_data(city):
    api_key = 'fcfbeda47e5cc82c41a5175171d1d2d9'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API Error: {e}")
        return None



def home(request):
    weather = None
    error = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = get_weather_data(city)
            if not weather:
                error = f"Could not retrieve weather data for '{city}'."
    else:
        form = CityForm()

    return render(request, 'home.html', {
        'form': form,
        'weather': weather,
        'error': error
    })
