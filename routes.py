import sys
sys.path.insert(0, './logic')

from flask import Flask, request
from car import Car

app = Flask(__name__)

# Taxi routes
@app.route('/car/release', methods=['POST', 'PUT'])
def handle_release_car():
	car = Car(request.form)
	print(car.get_position())
	return ''

# Passenger routes
@app.route('/passenger/order/create', methods=['POST', 'PUT'])
def handle_create_order():
	return ''

@app.route('/passenger/order/cancel', methods=['POST', 'PUT'])
def handle_cancel_order():
	return ''