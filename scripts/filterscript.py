for loc in data:
	temp = 0
	if 'categories' in loc:
		for categ in loc['categories']:
			if categ['alias'] == mycateg:
				temp = 1
	if temp == 1:
		print(loc['name'])