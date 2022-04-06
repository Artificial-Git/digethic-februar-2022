import requests

location_search = 'location/search/'
location = 'location/'

# Aufgabe 1.1
# https://www.metaweather.com/api/location/search/?query=Dresden
# url = 'https://www.metaweather.com/api/location/search/?query=(query)'
base_url = 'https://www.metaweather.com/api/'

params = {'query': 'Dresden'}

response = requests.get(base_url + location_search, params)

json = response.json()

print('response: ', response)
print('response code: ', response.status_code)
print('response json: ', json)
# [] json-Array. Im Array-Index 0 greifen wir auf woeid zu.
print('response woeid: ', json[0]['woeid'])


# Aufgabe 1.2
# https://www.metaweather.com/api/location/645686/
woeid = json[0]['woeid']

response_weather_dresden = requests.get(base_url + location + str(woeid))

print('response_weather_dresden code: ', response_weather_dresden.status_code)
print('response_weather_dresden json: ', response_weather_dresden.json())


# Aufgabe 1.3
# https://www.metaweather.com/api/location/645686/2019/3/8/

response_weather_dresden_march = requests.get(
    base_url + location + str(woeid) + '/2019/3/8')

print('response_weather_dresden_march: ',
      response_weather_dresden_march.json())
