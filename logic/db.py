from find import find_idx_by_id

##
# Fake database
#
class Database:
	def __init__(self):
		self.cars = []
		self.orders = []

	def find(self, collection):
		if collection == 'cars':
			return self.cars
		elif collection == 'orders':
			return self.orders
		else:
			return []

	def insert(self, collection, obj):
		if collection == 'cars':
			car_id = obj.get_id()
			idx = find_idx_by_id(self.cars, car_id)
			if idx == None:
				self.cars.append(obj)
				return True
			else:
				return False
		elif collection == 'orders':
			self.orders.append(obj)
			return True

	def remove(self, collection, obj, by_id=False):
		if collection == 'cars':
			car_id = obj.get_id() if not by_id else obj
			car_idx = find_idx_by_id(self.cars, car_id)
			if car_idx != None:
				del self.cars[car_idx]
				return True
			else:
				return False
		elif collection == 'orders':
			order_id = obj.get_id() if not by_id else obj
			order_idx = find_idx_by_id(self.orders, order_id)
			if order_idx != None:
				del self.orders[order_idx]
				return True
			else:
				return False

	def reset(self):
		del self.cars[:]
		del self.orders[:]