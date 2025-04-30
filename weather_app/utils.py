import requests

def get_weather_data(city):
    api_key = 'fcfbeda47e5cc82c41a5175171d1d2d9'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
