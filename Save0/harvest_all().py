def harvest_all():
	def harvest_one(x, y):
		goto(x, y)
		try_wait_harvest()
	
	for_each_cell(harvest_one)