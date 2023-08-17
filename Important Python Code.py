import requests, json
api_key = "65aa617fd027fd741420b0a6fdd3c082"
base_url = "http://api.openweathermap.org/data/2.5/weather?q="
city_name = input("City name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperatureK = y["temp"]
    current_temperatureL = (current_temperatureK - 273.15) * 9/5 + 32
    current_temperature = round(current_temperatureL, 1)
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_desc = z[0]["description"]

    print("Temperature = " + str(current_temperature) + "\n Atmospheric Pressure (in hPa unit)" + str(current_pressure) + "\n Humidity (in percentage) = " + str(current_humidity) + "\n Description = " + str(weather_desc))
else:
    print("City not found.")