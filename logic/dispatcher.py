from time import sleep
from threading import Lock

class Dispatcher:
	def __init__(self):
		self.free_cars = []
		self.orders = []
		self.orders_map = {}
		self.free_cars_map = {}
		self.lock = Lock()

	##
	#	Send new car to dispatching thread
	#	After release taxi can take a passenger
	#	@params:
	#		car - instance of Car
	#	@return: 
	#		http response (msg, code)
	#	
	def release_car(self, car):
		self.lock.acquire(1)
		id = car.get_id()
		res = ('', 200)

		if car.is_valid():
			if self.free_cars_map.get(id) == None:
				self.free_cars.append(car)
				self.free_cars_map[id] = len(self.free_cars) - 1
				res = ((
					'Taxi id=' + id + 
					': was released successfully'
				), 200)
			else:
				res = ((
					'Taxi id=' + id + 
					': the car has already released'
				), 200)
		else:
			res = ((
				'Taxi id=' + id + 
				': release car request data is invalid'
			), 400)

		self.lock.release()
		print(res[0])
		return res


	##
	#	Send new order to dispatching thread
	#	@params:
	#		passenger - instance of Passenger
	#	@return: 
	#		http response (msg, code)
	#
	def create_order(self, passenger):
		self.lock.acquire(1)
		id = passenger.get_id()
		res = ('', 200)

		if passenger.is_valid():
			if self.orders_map.get(id) == None:
				self.orders.append(passenger)
				self.orders_map[id] = len(self.orders) - 1
				res = ((
					'Passenger id=' + id + 
					': order was created successfully'
				), 200)
			else:
				res = ((
					'Passenger id=' + id + 
					': the order has already created'
				), 200)
		else:
			res = ((
				'Passenger id=' + id + 
				': create order request data is invalid'
			), 400)

		self.lock.release()
		print(res[0])
		return res

	##
	#	Remove order from dispatching thread
	#	@params:
	#		order_id - string
	#	@return: 
	#		http response (msg, code)
	#
	def cancel_order(self, order_id):
		self.lock.acquire(1)
		idx = self.orders_map.get(order_id)
		res = ('', 200)

		if idx == None:
			res = ((
				'Order wasn\'t canceled. ' + 
				'Couldn\'t find an order with id=' + order_id
			), 404)
		else:
			del self.orders[idx]
			del self.orders_map[order_id]
			res = ((
				'Passenger id=' + order_id + 
				': order was canceld successfully'
			), 200)

		self.lock.release()
		print(res[0])
		return res

	##
	#	Run dispatching taxis and orders thread
	##
	def start_dispatching(self):
		while True:
			while len(self.orders) > 0:
				order = self.take_order()
			sleep(1)