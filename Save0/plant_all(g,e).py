def plant_all(ground, entity):		
	def plant_one(x, y):
		goto(x, y)		
		if get_ground_type() != ground:
			till()							
		if get_entity_type() != entity:
			if not plant(entity):
				return False
	
	for_each_cell(plant_one)		
	return True