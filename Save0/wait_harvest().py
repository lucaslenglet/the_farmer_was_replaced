def wait_harvest():	
	while not can_harvest():
		wait(0.01)		
	harvest()	