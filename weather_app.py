import requests
from config import API_KEY

# Function to fetch the weather data from the API
def get_weather(city, country, api_key):
    # for API method, see: https://www.weatherapi.com/docs/
    # current weather
    base_url = "http://api.weatherapi.com/v1/current.json?"
    # choose temperature unit
    unit = input("Choose temperature unit (C for Celsius, F for Fahrenheit): ").upper()
    unit_param = 'metric' if unit == 'C' else 'imperial'  # 'metric' for Celsius, 'imperial' for Fahrenheit
    # Building the full API URL
    complete_url = f"{base_url}key={api_key}&q={city},{country}&aqi=no&units={unit_param}"
    
    # Sending a GET request to the API
    response = requests.get(complete_url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Extracting relevant information from the response
        if 'error' in data:
            print(f"Error: {data['error']['message']}")
            return
        
        # Parse the weather data
        location = data['location']
        current = data['current']
        
        city_name = location['name']
        country_name = location['country']
        temperature = current['temp_c']
        weather_description = current['condition']['text']
        humidity = current['humidity']
        wind_speed = current['wind_kph']
        
        # Display weather details
        print(f"Weather in {city_name}, {country_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
    else:
        print("City not found or invalid API key.")

# Main function to run the app
def main():
    api_key = API_KEY  # Replace this with your actual API key from OpenWeatherMap
    # Prompt to enter a city name
    location = input("Enter city and country (e.g., 'Paris, France'): ")

    if ',' in location:
        city, country = map(str.strip, location.split(','))
        get_weather(city, country, api_key)
    else:
        print("Please enter both city and country seperated by a comma.")

if __name__ == "__main__":
    main()