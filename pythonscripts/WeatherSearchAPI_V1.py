import requests
import json
from pprint import pprint

apikeyfile = open('apikey2.txt', 'r')
api_key = apikeyfile.read()

url = "http://api.openweathermap.org/data/2.5/forecast?id=4887398&APPID=" + str(api_key)

req = requests.get(url)

data = json.loads(req.text)["list"]

pprint(data[0])

count = 0
for day in data:
	if day["weather"][0]["main"] == "Rain":
		count += 1

print(count)

with open('WeatherTestDataV1.json', 'w') as outfile:
   json.dump(data, outfile, indent = 4)