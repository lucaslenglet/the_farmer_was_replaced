#goto_v1(6, 0)

def goto_v1(x, y):
	
	ws = get_world_size()
	
	if x > ws or y > ws:
		print("request out of bounds")
		return
	
	while is_not_at(x, y):
		cx = get_pos_x()
		cy = get_pos_y()
			
		if cx < x:
			move_x = East
		elif cx > x:
			move_x = West
		else:
			move_x = None
			
		if cy < y:
			move_y = North			
		elif cy > y:
			move_y = South
		else:
			move_y = None
			
		if not try_move(move_x):
			print("failed to move", move_x)
			return
			
		if not try_move(move_y):
			print("failed to move", move_y)
			return