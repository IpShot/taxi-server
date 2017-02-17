class Dispatcher:
	def __init__(self):
		self.free_cars = []
		self.orders = []

	def release_car(self, car):
		if car.is_valid():
			self.free_cars.append(car)
			msg = (
				'Taxi id=' + car.get_id() + 
				': was released successfully'
			)
			print(msg)
			return msg, 200
		else:
			msg = (
				'Taxi id=' + car.get_id() + 
				': release car request data is invalid'
			)
			print(msg)
			return msg, 400

	def create_order(self, passenger):
		if passenger.is_valid():
			self.orders.append(passenger)
			msg = (
				'Passenger id=' + passenger.get_id() + 
				': order was created successfully'
			)
			print(msg)
			return msg, 200
		else:
			msg = (
				'Passenger id=' + passenger.get_id() + 
				': create order request data is invalid'
			)
			print(msg)
			return msg, 400
		pass

	def cancel_order(self, passenger):
		pass