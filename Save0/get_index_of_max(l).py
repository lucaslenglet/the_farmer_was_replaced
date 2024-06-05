def get_index_of_max(l):
	return get_index(l, is_left_higher)

def is_left_higher(left, right):
	return left > right

def get_index(list, compare):	
	l = len(list)
	if l == 0:
		print("list is empty")
		return	
		
	index = 0
	item = list[index]
	
	for i in range(1, l):
		c = list[i]
		if compare(c, item):
			index = i
			item = c
	
	return index