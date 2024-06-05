def go_pumpkin_all():
	# Utilisation d'un tableau, car un int seul
	# ne serait pas maj au travers depuis la méthode
	# go(x, y), car surement passé par valeur et
	# non par référence
	status = [0]
	
	def go(x, y):
		goto(x, y)
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
		else:
			status[0] += 1
	
	for_each_cell(go)
	
	ws = get_world_size()	
	if ws * ws == status[0]:
		try_wait_harvest()