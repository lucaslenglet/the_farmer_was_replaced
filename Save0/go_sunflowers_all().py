# Optimisation possible :
# - Planter et mesurer en même temps ?
# - Rechercher le max le plus proche ?
# - Replanter/remesurer au passage ? non : lent

def go_sunflowers_all():
	plant_all(Grounds.Soil, Entities.Sunflower)
	measures = measure_all()
	
	v = 0
	
	while v != -1:
		max_index = get_index_of_max(measures)
		v = measures[max_index]
	
		if v == -1:
			quick_print("no more sunflowers")
			return
	
		(x, y) = index_to_coords(max_index)
		goto(x, y)
		wait_harvest()
		
		measures[max_index] = -1