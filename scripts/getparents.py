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
		parents[category] = number
	
	elif (catparents != [] and catparent not in parents):
		parents[catparent] = {category: number}
	
	elif (catparents != [] and catparent in parents):
		parents[catparent][category] = number
		#parents[catparent] = {category: number}
		
	


#topcat = sorted(parents.items(), key=lambda x: x[1], reverse=True)

#topcatdict = dict(topcat)

# with open('../json/chicagoparentcategorieslevel2.json', 'w') as outfile:
#  	json.dump(topcatdict, outfile, indent = 4)

pprint(parents)