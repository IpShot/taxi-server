class Dispatcher:
	def __init__(self):
		self.free_cars = []

	def release_car(self, car):
		print('Dispatch car release: ', car)
		self.free_cars.append(car)