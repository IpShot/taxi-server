import requests
from time import time
from random import random, uniform

def send_post(url, data):
	try:
		print(requests.post(url, data).text)
	except requests.exceptions.ConnectionError:
		print('Connection error. May be you forgot to start server?')
		exit()
	except requests.exceptions.RequestException as e:
		print('Error while trying to send POST %s', url)
		print(e)

# Constants
API_URL = 'http://127.0.0.1:5000'
RELEASE_CAR_URL = API_URL + '/car/release'
CREATE_ORDER_URL = API_URL + '/passenger/order/create'
CANCEL_ORDER_URL = API_URL + '/passenger/order/cancel'

##
# Generate taxis and passsenger
#
while True:
	c = random()
	p = random()
	t = random()
	co = random()

	# Generate taxi release
	if c > 0.5:
		car = {
			'id': str(c),
			'latitude': uniform(-180, 180),
			'longitude': uniform(-180, 180),
		}
		# Send release taxi request
		send_post(RELEASE_CAR_URL, car)

	# Generate passenger create order
	if p > 0.5:
		passenger = {
			'id': str(p),
			'latitude': uniform(-180, 180),
			'longitude': uniform(-180, 180),
		}
		if t > 0.5:
			passenger['timestamp'] = time() + uniform(0, 300)
		# Send create order request
		send_post(CREATE_ORDER_URL, passenger)

		# Send cancel order request
		if co > 0.9:
			send_post(CANCEL_ORDER_URL, { 'order_id': str(p) })




# send_post(
# 	'http://127.0.0.1:5000/car/release', 
# 	{
# 		'id': 'car-1', 
# 		'latitude': 88.4324,
# 		'longitude': 98.2133,
# 	}
# )

# Create passenger order post request
# send_post(
# 	'http://127.0.0.1:5000/passenger/order/create', 
# 	{
# 		'id': 'pas-1', 
# 		'latitude': 85.4324,
# 		'longitude': 92.2133,
# 		# 'timestamp': time(),
# 	}
# )

# Cancel passenger order post request
# send_post(
# 	'http://127.0.0.1:5000/passenger/order/cancel', 
# 	{
# 		'order_id': 'pas-1'
# 	}
# )

# send_post(
# 	'http://127.0.0.1:5000/passenger/order/cancel', 
# 	{
# 		'order_id': 'pas-2'
# 	}
# )

# send_post(
# 	'http://127.0.0.1:5000/passenger/order/cancel', 
# 	{
# 		'order_id': 'pas-1'
# 	}
# )