from positioned_object import PositionedObject

class Car(PositionedObject):
	def __init__(self, data):
		super(Car, self).__init__(data)
		self.free = True

	def is_free():
		return self.free

	def take():
		self.free = False

	def release():
		self.free = True