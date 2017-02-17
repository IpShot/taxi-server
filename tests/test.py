import requests

# Test release taxi post request
try:
	requests.post(
		'http://127.0.0.1:5000/car/release', 
		{
			'id': 'car-1', 
			'lattitude': 85.4324,
			'longtitude': 92.2133,
		}
	)
except requests.exceptions.ConnectionError:
	print('Connection error. May be you forgot to start server?')
except requests.exceptions.RequestException as e:
	print('Error while trying to send POST http://127.0.0.1:5000/car/release')
	print(e)