import requests
from time import time

def send_post(url, data):
	try:
		print(requests.post(url, data).text)
	except requests.exceptions.ConnectionError:
		print('Connection error. May be you forgot to start server?')
		exit()
	except requests.exceptions.RequestException as e:
		print('Error while trying to send POST %s', url)
		print(e)
		exit()

# Release taxi post request
send_post(
	'http://127.0.0.1:5000/car/release', 
	{
		'id': 'car-1', 
		'latitude': 85.4324,
		'longitude': 92.2133,
	}
)

# Create passenger order post request
send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-2',
		'latitude': 98.4324,
		'longitude': 108.2133,
		# 'timestamp': time(),
	}
)

send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-1', 
		'latitude': 88.4324,
		'longitude': 98.2133,
		# 'timestamp': time(),
	}
)

# Cancel passenger order post request
# send_post(
# 	'http://127.0.0.1:5000/passenger/order/cancel', 
# 	{
# 		'order_id': 'pas-1'
# 	}
# )

send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-2'
	}
)

# send_post(
# 	'http://127.0.0.1:5000/passenger/order/cancel', 
# 	{
# 		'order_id': 'pas-1'
# 	}
# )