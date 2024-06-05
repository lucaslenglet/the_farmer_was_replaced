def try_wait_harvest():
	if get_entity_type() == None:
		return
	while not can_harvest() and get_entity_type() != None:
		wait(0.01)		
	harvest()	