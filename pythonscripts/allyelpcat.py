import json
with open('yelpcategories.json') as json_file:
	yelpcategories = json.load(json_file)

cats = []

for cat in yelpcategories:
	if 'alias' in cat:
		if cat['alias'] not in cats:
			cats.append(cat['alias'])

with open('allyelpcategories.json', 'w') as outfile:
	json.dump(cats, outfile)