import sys
sys.path.append('../utils')

from send_post import send_post
from time import time


##
#  In the test passenger pas-1 should create
#  and cancel an order and shouldn't be delivered
#  by the car-1 taxi.
#  Also cancel requests from nonexistance passanger
#  pas-2, and already canceld pas-1 should be declined
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

# Create passenger order post request
send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-1', 
		'latitude': 85.4324,
		'longitude': 92.2133,
		'timestamp': time() + 1
	}
)

# Try to cancel nonexistance order
send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-2'
	}
)

# Try to cancel an order
send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-1'
	}
)

# Try to cancel the already canceld order
send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-1'
	}
)