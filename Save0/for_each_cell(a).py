def for_each_cell(action):
	ws = get_world_size()
	for x in range(ws):
		for y in range(ws):
			if x % 2 == 1:
				y = ws - y - 1
			r = action(x, y)
			if r != None:
				return r