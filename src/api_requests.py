#from unittest import result
#from urllib import request
import requests
# GET Request to https://www.metaweather.com/api/location/search/?query=dresden
params = {'query': 'dresden'}
headers = {"Content-Type": 'application/json'}
result = requests.get(
    'https://www.metaweather.com/api/location/search/', params=params, headers=headers
)

json = result.json()
print('JSON Response: ', json)
print('City name: ', json[0]['title'])
print('woeid: ', json[0]['woeid'])
