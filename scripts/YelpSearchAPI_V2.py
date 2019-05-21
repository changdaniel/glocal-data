import requests
import json
from pprint import pprint

with open('allyelpcategories.json') as json_file:
    yelpcategories = json.load(json_file)



apikeyfile = open('apikey.txt', 'r')
api_key = apikeyfile.read()

headers = {'Authorization': 'Bearer %s' % api_key}

params = {'location':'Chicago','offset': 0}

url='https://api.yelp.com/v3/businesses/search'

req = requests.get(url, params=params, headers=headers)
json.loads(req.text)

biginfolist = [];



for category in yelpcategories:
	params = {'location':'Chicago', 'categories': '' + category, 'limit':50}
	req = requests.get(url, params=params, headers=headers)
	infodict = json.loads(req.text)
	infolist = infodict.get('businesses')

	if infolist is None:
		continue
	else:
		biginfolist = biginfolist + infolist


print(len(biginfolist))


with open('ChicagoSearchDataV3.json', 'w') as outfile:
    json.dump(biginfolist, outfile, indent = 4)