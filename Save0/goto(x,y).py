#goto_v1(6, 0)

def goto(x, y):	
	ws = get_world_size()
	
	if x > ws or y > ws:
		print("request out of bounds")
		return
	
	cx = get_pos_x()		
	bmx = get_best_move(cx, x, ws)
	if not move_x(bmx):
		print("failed to move x : ", move_x)
		return
		
	cy = get_pos_y()	
	bmy = get_best_move(cy, y, ws)
	if not move_y(bmy):
		print("failed to move y : ", bmy)
		return
	
	if is_not_at(x, y):
		print("wtf!")
		return	