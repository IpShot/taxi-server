##
# The class is using for dispatching http request 
#
class Dispatcher:
	def __init__(self, db, lock):
		self.db = db
		self.lock = lock
				
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
		car_id = car.get_id()
		res = ('', 200)

		if car.is_valid():
			resp = self.db.insert('cars', car)
			if resp == True:
				res = ((
					'Taxi id=' + car_id + 
					': was released successfully'
				), 200)
			else:
				res = ((
					'Taxi id=' + car_id + 
					': the car has already released'
				), 200)
		else:
			res = ((
				'Taxi id=' + car_id + 
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
		pas_id = passenger.get_id()
		res = ('', 200)

		if passenger.is_valid():
			resp = self.db.insert('orders', passenger)
			if resp == True:
				res = ((
					'Passenger id=' + pas_id + 
					': order was created successfully'
				), 200)
			else:
				res = ((
					'Passenger id=' + pas_id + 
					': the order has already created'
				), 200)
		else:
			res = ((
				'Passenger id=' + pas_id + 
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
		resp = self.db.remove('orders', order_id, by_id=True)
		res = ('', 200)

		if resp:
			res = ((
				'Passenger id=' + order_id + 
				': order was canceld successfully'
			), 200)
		else:
			res = ((
				'Order wasn\'t canceled. ' + 
				'Couldn\'t find an order with id=' + order_id
			), 404)

		self.lock.release()
		print(res[0])
		return res

	## 
	# Using in tests for reset data from previous tests
	#
	def reset(self):
		self.lock.acquire(1)
		self.db.reset()
		self.lock.release()
		msg = 'Data was reset successfully'
		print(msg)
		return msg, 200