from converter import conv

class PositionedObject:
	def __init__(self, data):
		self.id = conv(data['id'], str)
		self.lat = conv(data['latitude'], float)
		self.lon = conv(data['longitude'], float)

	def is_valid(self):
		return (
			self.id != None 
			and self.lat != None 
			and self.lon != None
		)

	def get_id(self):
		return self.id

	##
	# Return lattitude and longtitude coordinates
	#
	def get_coordinates(self):
		return {
			'lon': self.lon,
			'lat': self.lat,
		}