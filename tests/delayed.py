import sys
sys.path.append('../utils')

from send_post import send_post
from time import time


##
#  In the test passenger pas-2 should be delivered 
#  first by the nearest car-2 taxi then passenger pas-1 
#  should be delivered by car-1
##


# Reset data app from previous tests
send_post('http://127.0.0.1:5000/reset', {})

# Create passenger order post request
send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-1', 
		'latitude': 85.4324,
		'longitude': 92.2133,
		'timestamp': time() + 2
	}
)

send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-2', 
		'latitude': 85.4324,
		'longitude': 92.2133,
		'timestamp': time() + 1
	}
)

# Release taxi post request
send_post(
	'http://127.0.0.1:5000/car/release', 
	{
		'id': 'car-2', 
		'latitude': 98.4324,
		'longitude': 108.2133,
	}
)

send_post(
	'http://127.0.0.1:5000/car/release', 
	{
		'id': 'car-1', 
		'latitude': 108.4324,
		'longitude': 198.2133,
	}
)