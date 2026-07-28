#Build an Automated Extract-Load (EL) pipeline.
#Connect to a weather API (e.g., wttr.in), prompt for a city, extract temp/humidity from JSON, and append it to weather.csv.

import requests

# 1. Extraction
def extract_weather(city):
    weather = requests.get(f"https://wttr.in/{city}?format=j1")
    if weather.status_code == 200:
        return weather.json()  # To return the dictionary payload
    else:
        print(f"Failed to retrieve data. Status code: {weather.status_code}")
        return None

# 2. Parsing
def parse_weather(raw_json):
    current = raw_json["current_condition"][0]
    humidity = current["humidity"]
    temp = current["temp_C"]

    area_info = raw_json["nearest_area"][0]
    final_city = area_info["areaName"][0]["value"]

    # Format into a CSV row and return it
    return f"{final_city},{humidity},{temp}\n"

# 3. Loading
def load_to_csv(data_row):
    file_path = "C:/Users/Berna/OneDrive/Documents/CLMagno_DE_Bootcamp/Python Exercises/weather.csv"
    with open(file_path, "a") as f:
        f.write(data_row)
    print("Data appended successfully!")



city_input = input("Enter a city name: ")
raw_data = extract_weather(city_input)

if raw_data:
    row = parse_weather(raw_data)
    load_to_csv(row)