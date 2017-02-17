class Dispatcher:
	def __init__(self):
		self.free_cars = []
		self.orders = []
		self.orders_map = {}
		self.free_cars_map = {}

	def release_car(self, car):
		id = car.get_id()
		if car.is_valid():
			self.free_cars.append(car)
			self.free_cars_map[id] = len(self.free_cars)
			msg = (
				'Taxi id=' + id + 
				': was released successfully'
			)
			print(msg)
			return msg, 200
		else:
			msg = (
				'Taxi id=' + id + 
				': release car request data is invalid'
			)
			print(msg)
			return msg, 400

	def create_order(self, passenger):
		id = passenger.get_id()
		if passenger.is_valid():
			self.orders.append(passenger)
			self.orders_map[id] = len(self.orders)
			msg = (
				'Passenger id=' + id + 
				': order was created successfully'
			)
			print(msg)
			return msg, 200
		else:
			msg = (
				'Passenger id=' + id + 
				': create order request data is invalid'
			)
			print(msg)
			return msg, 400

	def cancel_order(self, passenger):
		id = passenger.get_id()
		if passenger.is_valid():
			idx = self.orders_map[id]
			del self.orders[idx]
			msg = (
				'Passenger id=' + id + 
				': order was canceld successfully'
			)
			print(msg)
			return msg, 200
		else:
			msg = (
				'Passenger id=' + id + 
				': cancel order request data is invalid'
			)
			print(msg)
			return msg, 400