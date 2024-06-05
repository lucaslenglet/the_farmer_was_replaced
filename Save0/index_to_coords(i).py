def index_to_coords(i):
	ws = get_world_size()
	y = i % ws
	x = i // ws
	return (x, y)