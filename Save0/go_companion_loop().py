# Il y a un bug quelque part, car la methode get_companion() est parfois
# appelée sur une cell sans plante
def go_companion_loop():
	buffer_limit = 5
	buffer = []
	
	start_e = random_elem([Entities.Bush, Entities.Grass, Entities.Tree, Entities.Carrots])
	
	plant(start_e)
	
	while True:
		curr = get_pos()
		buffer.insert(0, curr)
		
		(cmp_e, cmp_x, cmp_y) = get_companion()
		
		goto(cmp_x, cmp_y)	
		
		if get_entity_type() != None:
			try_wait_harvest()
	
		if not plant(cmp_e):
			print("failed to plant")
			return
		else:
			if get_water() < 0.5:
				use_item(Items.Water_Tank)
		
		if len(buffer) >= buffer_limit:
			tgt = buffer.pop()
			goto(tgt[0], tgt[1])
			try_wait_harvest()
			goto(cmp_x, cmp_y)