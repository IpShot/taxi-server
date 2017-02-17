import sys
sys.path.append('./logic')
sys.path.append('./utils')

from flask import Flask, request
from car import Car
from passenger import Passenger
from dispatcher import Dispatcher

app = Flask(__name__)
dispatcher = Dispatcher()

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
	passenger = Passenger(request.form)
	return dispatcher.cancel_order(passenger)

if __name__ == '__main__':
	app.run(debug=True)