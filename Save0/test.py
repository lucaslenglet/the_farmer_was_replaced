clean_for_test()
	
def clean_for_test():
	clear()
	def apply_turf(x, y):
		goto(x, y)
		till()
	for_each_cell(apply_turf)
	mid = get_world_size() // 2
	goto(mid, mid)