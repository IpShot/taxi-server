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
			self.free_cars_map[id] = len(self.free_cars) - 1
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
			self.orders_map[id] = len(self.orders) - 1
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

	def cancel_order(self, order_id):
		idx = self.orders_map.get(order_id)
		if idx == None:
			msg = (
				'Order wasn\'t canceled. ' + 
				'Couldn\'t find an order with id=' + order_id
			)
			print(msg)
			return msg, 404
		else:
			del self.orders[idx]
			msg = (
				'Passenger id=' + order_id + 
				': order was canceld successfully'
			)
			print(msg)
			return msg, 200