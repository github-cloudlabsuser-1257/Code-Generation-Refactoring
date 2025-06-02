import requests

def fetch_weather(api_key, city):
    """
    Fetches weather data for a given city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        print(f"Weather in {city}:")
        print(f"Temperature: {main.get('temp', 'N/A')}°C")
        print(f"Condition: {weather.get('description', 'N/A').title()}")
    else:
        print("Failed to fetch weather data. Please check the city name or API key.")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    fetch_weather(api_key, city)