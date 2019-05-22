import json
with open('yelpcategories.json') as json_file:
    yelpcategories = json.load(json_file)

with open('categories.json') as json_file:
    categories = json.load(json_file)

with open('ChicagoSearchDataV4.json') as json_file:
    data = json.load(json_file)


banlist = []

nonrestaurant = []


for key in yelpcategories:
	if len(key['parents']) > 0:
		##print(key['parents'][0])
		if key['parents'][0] == 'restaurants' or key['parents'][0] == 'food' or  key['parents'][0] == 'bars':
			banlist.append(key['alias'])
		if key['alias'] == 'bars':
			banlist.append(key['alias'])


for key in yelpcategories:
	if len(key['parents']) > 0:
		##print(key['parents'][0])
		if key['parents'][0] in banlist:
			banlist.append(key['alias'])


categories = {}

for loc in data:
	if 'categories' in loc:
		for categ in loc['categories']:
			if categ['alias'] not in banlist:
				if categ['alias'] not in categories:
					categories[categ['alias']] = 1
				else:
					categories[categ['alias']] += 1

topcat = sorted(categories.items(), key=lambda x: x[1], reverse=True)


topcatdict = dict(topcat)

print(len(topcatdict))

with open('chicagononfood.json', 'w') as outfile:
	json.dump(topcatdict, outfile, indent = 4)