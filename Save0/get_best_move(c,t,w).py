def get_best_move(curr, to, world_size):
	if curr == to:
		return 0
		
	from_op = curr - to + world_size
	direct = to - curr
		
	if from_op < direct:
		return -1 * from_op
	else:
		return direct