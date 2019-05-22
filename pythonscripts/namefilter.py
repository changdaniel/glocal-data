import json
with open('ChicagoSearchDataV4.json') as json_file:
	data = json.load(json_file)

locs = []

for loc in data:
	if 'name' in loc:
		if loc['name'] not in locs:
			locs.append(loc)

print(len(locs))


locs2 = []

for loc in locs:
	if 'id' in loc:
		if loc['id'] not in locs2:
			locs2.append(loc)

print(len(locs2))


with open('ChicagoSearchDataV4.json', 'w') as outfile:
	json.dump(locs2, outfile, indent = 4)