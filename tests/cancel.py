import sys
sys.path.append('../utils')
from send_post import send_post


# Create passenger order post request
send_post(
	'http://127.0.0.1:5000/passenger/order/create', 
	{
		'id': 'pas-1', 
		'latitude': 85.4324,
		'longitude': 92.2133,
	}
)

# Try to cancel an order
send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-1'
	}
)

# Try to cancel nonexistance order
send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-2'
	}
)

# Try to cancel the already canceld order
send_post(
	'http://127.0.0.1:5000/passenger/order/cancel', 
	{
		'order_id': 'pas-1'
	}
)