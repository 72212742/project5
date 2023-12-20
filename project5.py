import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city}: {temperature}°C, {description}")
    else:
        print(f"Error: Unable to fetch weather data for {city}")

# Example usage:
get_weather("London")
