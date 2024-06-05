# Stops execution for n amount of seconds
def wait(n):
	time_to_let_go = get_time() + n
	
	while get_time() < time_to_let_go:
		pass