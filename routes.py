from flask import Flask
app = Flask(__name__)

# Taxi routes
@app.route('/taxi/release', methods=['POST', 'PUT'])
def handle_release_taxi():
  return ''

# Passenger routes
@app.route('/passenger/order/create', methods=['POST', 'PUT'])
def handle_create_order():
	return ''

@app.route('/passenger/order/cancel', methods=['POST', 'PUT'])
def handle_cancel_order():
	return ''