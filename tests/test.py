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
		'lattitude': 85.4324,
		'longtitude': 92.2133,
	}
)

# Create passenger order post request
send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-1', 
		'lattitude': 85.4324,
		'longtitude': 92.2133,
		'timestamp': time(),
	}
)