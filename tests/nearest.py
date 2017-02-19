import sys
sys.path.append('../utils')
from send_post import send_post


##
#  In the test passenger pas-1 should be 
#  delivered by the nearest car-2 taxi
##


# Reset data app from previous tests
send_post('http://127.0.0.1:5000/reset', {})

# Release taxi post request
send_post(
	'http://127.0.0.1:5000/car/release', 
	{
		'id': 'car-1', 
		'latitude': 108.4324,
		'longitude': 198.2133,
	}
)

send_post(
	'http://127.0.0.1:5000/car/release', 
	{
		'id': 'car-2', 
		'latitude': 88.4324,
		'longitude': 98.2133,
	}
)

send_post(
	'http://127.0.0.1:5000/car/release', 
	{
		'id': 'car-3', 
		'latitude': 108.4324,
		'longitude': 198.2133,
	}
)

# Create passenger order post request
send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-1', 
		'latitude': 85.4324,
		'longitude': 92.2133,
	}
)