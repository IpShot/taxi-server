from converter import conv

class PositionedObject:
	def __init__(self, data):
		self.id = conv(data['id'], str)
		self.lat = conv(data['lattitude'], float)
		self.lon = conv(data['longtitude'], float)

	def is_valid(self):
		return (
			self.id != None 
			and self.lat != None 
			and self.lon != None
		)

	def get_id(self):
		return self.id

	def get_lat(self):
		return self.lat

	def get_lon(self):
		return self.lon