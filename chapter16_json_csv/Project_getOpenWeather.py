# getOpenWeather.py - Prints the weather for a location from the command line.

APP_ID = "9e403825f6f3e598f9eab010a76cf06b"

import sys, json, requests

# Compute location from command line arguments.

if len(sys.argv) != 3:
    print("Usage: getOpenWeather.py city_name 2-letter_country_code")
    sys.exit()
location = f"{sys.argv[1]},{sys.argv[2]}"

# Download the JSON data from OpenWeatherMap.org's API.

url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&APPID={APP_ID}"

try:
    res = requests.get(url)
    res.raise_for_status()

    # Parse the JSON response.
    weather_data = json.loads(res.text)

    # Extract and display the weather information.
    print("Weather in {} for the next 3 days:".format(location))
    for day in weather_data["list"]:
        date = day["dt"]
        temperature = day["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        description = day["weather"][0]["description"]
        print(
            f"Date: {date}, Temperature: {temperature:.2f}°C, Description: {description}"
        )
except requests.exceptions.RequestException as e:
    print("An error occurred: ", e)
