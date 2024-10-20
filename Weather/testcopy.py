import requests
import datetime

# Your API key and the city for which you want the weather
API_KEY = 'de2beab57661f8e1fccd157c3b6ab24c'
CITY = 'New Delhi'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Fetching the weather data
response = requests.get(URL)
data = response.json()

# Parsing the necessary fields
main_condition = data['weather'][0]['main']  # Main weather condition
temp = data['main']['temp']  # Current temperature in Celsius
feels_like = data['main']['feels_like']  # Perceived temperature in Celsius
timestamp = data['dt']  # Unix timestamp of data update

# Convert Unix timestamp to human-readable time
readable_time = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Printing the results
print(f"Weather Condition: {main_condition}")
print(f"Temperature: {temp} °C")
print(f"Feels Like: {feels_like} °C")
print(f"Last Updated: {readable_time}")
