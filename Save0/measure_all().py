def measure_all():
	ws = get_world_size()	
	mesures = empty_list(ws * ws)
	def measure_one(x, y):
		goto(x, y)
		m = measure()
		if m == None:
			m = -1
		i = coords_to_index(x, y)
		mesures[i] = m
	
	for_each_cell(measure_one)
	return mesures