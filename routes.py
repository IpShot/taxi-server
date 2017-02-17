import sys
sys.path.append('./logic')
sys.path.append('./utils')

from flask import Flask, request
from threading import Thread
from car import Car
from passenger import Passenger
from dispatcher import Dispatcher

app = Flask(__name__)
dispatcher = Dispatcher()

# Create taxis and orders dispatching thread
dispatcher_daemon = Thread(target=dispatcher.start_dispatching)
dispatcher_daemon.daemon = True
dispatcher_daemon.start()

# Taxi routes
@app.route('/car/release', methods=['POST', 'PUT'])
def handle_release_car():
	car = Car(request.form)
	return dispatcher.release_car(car)

# Passenger routes
@app.route('/passenger/order/create', methods=['POST', 'PUT'])
def handle_create_order():
	passenger = Passenger(request.form)
	return dispatcher.create_order(passenger)

@app.route('/passenger/order/cancel', methods=['POST', 'PUT'])
def handle_cancel_order():
	order_id = str(request.form['order_id'])
	return dispatcher.cancel_order(order_id)

# Start flask app
if __name__ == '__main__':
	app.run(debug=True)