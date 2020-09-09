import requests
import pprint

api = "b05eab33c773c6b1ba26819d9180c8bf"

def weatherApp():
	print("Weather Checker V1.0 \n")
	city = input("Enter City: ")
	url = "http://api.openweathermap.org/data/2.5/weather"
	params = {"q":city, "appid":api}
	r = requests.get(url= url, params = params)
	data_list = r.json()
	
	#pprint.pprint(data_list)
	#print(data_list["weather"][0]["main"])
	

	humidity = data_list['main']["humidity"]
	city_name = data_list["name"]
	country_code = data_list["sys"]["country"]
	weather_desc = data_list["weather"][0]["description"]
	weather_main = data_list["weather"][0]["main"]
	
	print("\nWeather Forecast for today! \n")
	print(f"Country Code : {country_code}\nCity Name: {city_name}\nHumidity: {humidity}\nWeather : {weather_main} ({weather_desc})")

weatherApp()	
