from converter import conv

class Car:
	def __init__(self, data):
		self.id = conv(data['id'], str)
		self.lat = conv(data['lattitude'], float)
		self.lot = conv(data['longtitude'], float)

	def is_valid(self):
		return (
			self.id != None 
			and self.lat != None 
			and self.lot != None
		)