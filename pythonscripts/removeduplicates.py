import json

with open('ChicagoSearchDataV3.json') as json_file:
    data = json.load(json_file)


d = data
test = [i for n, i in enumerate(d) if i not in d[n + 1:]]

print(len(test))

# bigdatadict = {}
# bigdataarr = []

# for loc in data:
# 	if loc['id'] not in bigdatadict:
# 		bigdatadict[loc['id']] = loc
# 		bigdataarr.append(loc)


# print(len(bigdataarr))


#with open('ChicagoSearchDataV4.json', 'w') as outfile:
#	json.dump(bigdataarr, outfile, indent = 4)