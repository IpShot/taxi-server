from invariant import invariant

class Car:
	def __init__(self, data):
		self.id = data['id']
		self.lot = float(data['longtitude'])
		self.lat = float(data['lattitude'])

	def is_valid(self):
		car_id = isinstance(self.id, str)
		lot = isinstance(self.lot, (int, float))
		lat = isinstance(self.lat, (int, float))
		try:
			invariant(
				car_id,
				'Got car id with wrong type: %s' % self.id,
			)
			invariant(
				lot,
				'Got longtitude with wrong type: %f' % self.lot,
			)
			invariant(
				lat,
				'Got lattitude with wrong type: %f' % self.lat,
			)
			print('valid')
			return True
		except ValueError as e:
			print (e)
			return False