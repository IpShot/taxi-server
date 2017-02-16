def invariant(cond, msg):
	if not cond:
		print(msg)
		raise ValueError