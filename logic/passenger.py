from converter import conv
from positioned_object import PositionedObject

class Passenger(PositionedObject):
	def __init__(self, data):
		super(Passenger, self).__init__(data)
		self.time = conv(data['timestamp'], float)

	def is_valid(self):
		return (
			self.id != None 
			and self.lat != None 
			and self.lon != None
			and self.time != None
		)