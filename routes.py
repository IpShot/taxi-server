import sys
sys.path.append('./logic')
sys.path.append('./utils')

from flask import Flask, request
from car import Car
from dispatcher import Dispatcher

app = Flask(__name__)
dispatcher = Dispatcher()

# Taxi routes
@app.route('/car/release', methods=['POST', 'PUT'])
def handle_release_car():
	car = Car(request.form)
	if car.is_valid():
		dispatcher.release_car(car)
	return ''

# Passenger routes
@app.route('/passenger/order/create', methods=['POST', 'PUT'])
def handle_create_order():
	return ''

@app.route('/passenger/order/cancel', methods=['POST', 'PUT'])
def handle_cancel_order():
	return ''