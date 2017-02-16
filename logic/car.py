class Car:
	def __init__(self, data):
		self.id = data['id']
		self.lot = data['longtitude']
		self.lat = data['lattitude']

	def get_position(self):
		return {
			'longtitude': self.lot, 
			'lattitude': self.lat,
		}