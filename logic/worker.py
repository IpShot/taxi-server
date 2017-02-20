from time import time, sleep
from calculator import distance

##
# Searching the nearest to the passenger free taxi
#
def _find_nearest_taxi(order, cars):
	if len(cars) > 1:
		passenger_coordinates = order.get_coordinates()
		nearest_taxi = cars[0]
		dist = distance(
			passenger_coordinates,
			nearest_taxi.get_coordinates(),
		)
		for i in range(1, len(cars)):
			car = cars[i]
			new_dist = distance(
				passenger_coordinates,
				car.get_coordinates(),
			)
			if (new_dist < dist):
				dist = new_dist
				nearest_taxi = car
		return nearest_taxi
	elif len(cars) == 1:
		return cars[0]
	else:
		return None

##
# The class is using for searching taxis for each order
#
class Worker():
	def __init__(self, db, lock):
		self.db = db
		self.lock = lock

	##
	# Searching taxi for an order
	#	
	def _dispatch_order(self, order, cars):
		filing_time = order.get_time()

		# If order has no deferred time or
		# deffered time has already come
		# then passenger want to take taxi now
		if filing_time == None or time() >= filing_time:
			taxi = _find_nearest_taxi(order, cars)

			if taxi == None:
				return

			# Remove binded order and taxi
			self.db.remove('orders', order)
			self.db.remove('cars', taxi)

			print(
				'Taxi id=%s and Passenger id=%s were dispatched successfully'
				% (taxi.get_id(), order.get_id())
			)
		else:
			return

	##
	# Run dispatching taxis and orders thread
	#
	def run(self):
		while True:
			self.lock.acquire(1)
			cars = self.db.find('cars')
			orders = self.db.find('orders')
			# If we have at least one free taxi
			if len(cars) > 0:
				for order in orders:
					self._dispatch_order(order, cars)
			self.lock.release()
			sleep(1)