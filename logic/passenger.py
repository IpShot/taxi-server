from converter import conv
from positioned_object import PositionedObject

class Passenger(PositionedObject):
	def __init__(self, data):
		super(Passenger, self).__init__(data)
		time = data.get('timestamp')
		self.time = conv(time, float)
		self._validate_time(time)
		
	def _validate_time(self, time):
		if time != None and self.time == None:
			self.valid = False
		else:
			self.valid = True

	def is_valid(self):
		return (
			self.id == None
			and self.lat != None 
			and self.lon != None
			and self.valid
		)

	def get_time(self):
		return self.time