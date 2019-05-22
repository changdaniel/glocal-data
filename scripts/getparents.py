import json
from pprint import pprint

with open('../json/chicagocategories.json') as json_file:
    chicago = json.load(json_file)

with open('../json/yelpcategories.json') as json_file:
    yelp = json.load(json_file)

parents = {}

for category, number in chicago.items():
	
	for cat in yelp:

		if cat['alias'] == category:
			catparents = cat['parents']
			
			if(catparents != []):
				catparent = catparents[0]
			else:
				catparent = "string";

	if (catparents == [] and category not in parents):
		pass
		#parents[category] = number
	
	elif (catparents != [] and catparent not in parents):
		parents[catparent] = {category: number}
	
	elif (catparents != [] and catparent in parents):
		parents[catparent][category] = number
		#parents[catparent] = {category: number}
		
	


#topcat = sorted(parents.items(), key=lambda x: x[1], reverse=True)

#topcatdict = dict(topcat)

with open('chicagocategorytree.json', 'w') as outfile:
  	json.dump(parents, outfile, indent = 4)

pprint(parents)