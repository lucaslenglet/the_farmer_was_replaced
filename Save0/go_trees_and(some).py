def go_trees_and(some):
	
	def go(x, y):
		goto(x, y)
		try_wait_harvest()
		
		if x % 2 == y % 2:					
			plant(Entities.Tree)
		else:
			if get_entity_type() != some:
				plant(some)
	
	for_each_cell(go)