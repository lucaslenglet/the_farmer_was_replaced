def go_all(g, e):
	if not plant_all(g, e):
		harvest_all()
		return
	harvest_all()