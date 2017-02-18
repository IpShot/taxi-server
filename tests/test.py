import sys
sys.path.append('../utils')

from time import time, sleep
from random import random, uniform
from send_post import send_post

# Constants
API_URL = 'http://127.0.0.1:5000'
RELEASE_CAR_URL = API_URL + '/car/release'
CREATE_ORDER_URL = API_URL + '/passenger/order/create'
CANCEL_ORDER_URL = API_URL + '/passenger/order/cancel'

##
# Generate taxis and passsengers
#
while True:
	sleep(0.5)
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