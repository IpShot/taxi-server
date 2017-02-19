import sys
sys.path.append('./logic')
sys.path.append('./utils')

from flask import Flask, request
from threading import Thread
from car import Car
from passenger import Passenger
from dispatcher import Dispatcher
import logging

app = Flask(__name__)
dispatcher = Dispatcher()

# Create taxis and orders dispatching thread
dispatching = Thread(target=dispatcher.start_dispatching)
dispatching.daemon = True
dispatching.start()

# Change logger to log only errors
# So, we can see our dispatcher only clear logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Taxi routes
@app.route('/car/release', methods=['POST'])
def handle_release_car():
	car = Car(request.form)
	return dispatcher.release_car(car)

# Passenger routes
@app.route('/passenger/order/create', methods=['POST'])
def handle_create_order():
	passenger = Passenger(request.form)
	return dispatcher.create_order(passenger)

@app.route('/passenger/order/cancel', methods=['POST'])
def handle_cancel_order():
	order_id = str(request.form['order_id'])
	return dispatcher.cancel_order(order_id)

# Using in tests
@app.route('/reset', methods=['POST'])
def reset_dispatcher_data():
	return dispatcher.reset()

# Start flask app
if __name__ == '__main__':
	app.run(debug=True)