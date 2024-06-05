def move_on_axis(n, axis_a, axis_b):
	if n == 0:
		return True
	elif n < 0:
		for i in range(0, n, -1):
			if not move(axis_b):
				return False
	else:
		for i in range(0, n):
			if not move(axis_a):
				return False
	return True