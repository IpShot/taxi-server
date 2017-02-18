from time import time, sleep
from threading import Lock
from calculator import distance

##
# Searching the element index in the list by id
#
def find_idx_by_id(l, id):
	return next(
		(i for i, x in enumerate(l) if x.id == id), 
		None,
	)

##
# The class is dispatching http request 
# and searching taxis for each order
#
class Dispatcher:
	def __init__(self):
		self.free_cars = []
		self.orders = []
		self.lock = Lock()

	def _find_nearest_taxi(self, order):
		if len(self.free_cars) > 1:
			passenger_coordinates = order.get_coordinates()
			nearest_taxi = self.free_cars[0]
			dist = distance(
				passenger_coordinates,
				nearest_taxi.get_coordinates(),
			)
			for i in range(1, len(self.free_cars)):
				car = self.free_cars[i]
				new_dist = distance(
					passenger_coordinates,
					car.get_coordinates(),
				)
				if (new_dist < dist):
					dist = new_dist
					nearest_taxi = car
			return nearest_taxi
		elif len(self.free_cars) == 1:
			return self.free_cars[0]
		else:
			return None

	##
	# Searching taxi for an order
	#	
	def _dispatch_order(self, order):
		filing_time = order.get_time()

		# If order has no deferred time or
		# deffered time has already come
		# then passenger want to take taxi now
		if filing_time == None or time() >= filing_time:
			taxi = self._find_nearest_taxi(order)

			if taxi == None:
				return

			# Remove binded order and taxi
			order_id = order.get_id()
			order_idx = find_idx_by_id(self.orders, order_id)
			del self.orders[order_idx]

			taxi_id = taxi.get_id()
			taxi_idx = find_idx_by_id(self.free_cars, taxi_id)
			del self.free_cars[taxi_idx]

			print(
				'Taxi id=%s and Passenger id=%s were dispatched successfully'
				% (taxi_id, order_id)
			)
		else:
			return
				
	##
	# Send new car to dispatching thread
	# After release taxi can take a passenger
	# @params:
	#   car - instance of Car
	# @return: 
	#   http response (msg, code)
	#	
	def release_car(self, car):
		self.lock.acquire(1)
		id = car.get_id()
		res = ('', 200)

		if car.is_valid():
			idx = find_idx_by_id(self.free_cars, id)
			if idx == None:
				self.free_cars.append(car)
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
	# Send new order to dispatching thread
	# @params:
	#   passenger - instance of Passenger
	# @return: 
	#   http response (msg, code)
	#
	def create_order(self, passenger):
		self.lock.acquire(1)
		id = passenger.get_id()
		res = ('', 200)

		if passenger.is_valid():
			idx = find_idx_by_id(self.orders, id)
			if idx == None:
				self.orders.append(passenger)
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
	# Remove order from dispatching thread
	# @params:
	#   order_id - string
	# @return: 
	#   http response (msg, code)
	#
	def cancel_order(self, order_id):
		self.lock.acquire(1)
		idx = find_idx_by_id(self.orders, order_id)
		res = ('', 200)

		if idx == None:
			res = ((
				'Order wasn\'t canceled. ' + 
				'Couldn\'t find an order with id=' + order_id
			), 404)
		else:
			del self.orders[idx]
			res = ((
				'Passenger id=' + order_id + 
				': order was canceld successfully'
			), 200)

		self.lock.release()
		print(res[0])
		return res

	##
	# Run dispatching taxis and orders thread
	#
	def start_dispatching(self):
		while True:
			self.lock.acquire(1)
			# If we have at least one free taxi
			if len(self.free_cars) > 0:
				for order in self.orders:
					self._dispatch_order(order)
			self.lock.release()
			sleep(1)