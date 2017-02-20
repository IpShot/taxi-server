import sys
sys.path.append('./logic')
sys.path.append('./utils')

from flask import Flask, request
from threading import Thread, Lock
from car import Car
from passenger import Passenger
from dispatcher import Dispatcher
from worker import Worker
from db import Database
import logging


app = Flask(__name__)

# Create thread lock for manage access 
# to db from dispatcher and worker 
lock = Lock()

# Create fake database
db = Database()

# Create main handlers
dispatcher = Dispatcher(db, lock)
worker = Worker(db, lock)

# Create taxis and orders dispatching thread
dispatching = Thread(target=worker.run)
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