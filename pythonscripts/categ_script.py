import json
with open('ChicagoDetailsDataV2.json') as json_file:
    data = json.load(json_file)

categories = {}

for loc in data:
	if 'categories' in loc:
		for categ in loc['categories']:
			if categ['alias'] in categories:
				categories[categ['alias']] += 1
			else:
				categories[categ['alias']] = 1

topcat = sorted(categories.items(), key=lambda x: x[1], reverse=True)

topcatdict = dict(topcat)

with open('chicategories.json', 'w') as outfile:
	json.dump(topcatdict, outfile)