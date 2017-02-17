def conv(data, type):
	try:
		return type(data)
	except ValueError as e:
		print(e)
		return None