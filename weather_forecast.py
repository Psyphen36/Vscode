# import requests

# def weather(api_key, city_code):
# 	api_url = 'https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=5c8a0ea42ecc44a5a20c913af905f098&include=minutely'
# 	params = {
# 		'id': city_code,
# 		'units': 'metric',
# 		'appid': api_key
# 	}
# 	response = requests.get(api_url, params=params)
# 	data = response.json()
# 	return data


# key = '5c8a0ea42ecc44a5a20c913af905f098'
# pin_code = 486001

# weather_data = weather(key, pin_code)
# print(weather_data)


import requests
# import json

API_KEY = '3d172fcaf7d9774dcaf7029982f01488'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'
# def get_weather(api_key, location):


# params = {
#     "q": location,
#     "appid": api_key,
#     "units": "metric"
# }

city = input("Enter a location: ")
request_url = f'{API_URL}?appid={API_KEY}={city}'
response = requests.get(request_url)
data = response.json()

if response.status_code == 200:
    print(f"Weather forecast for {city}:")
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    print('Weather: ',weather)
    print('Temperature: ',temperature, 'celsius')
else:
    print('An Error Occurred!!')
    print(data)
# def main():
    

#     get_weather(key, location)

# if __name__ == "__main__":
#     main()
