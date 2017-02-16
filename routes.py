from flask import Flask
app = Flask(__name__)

# Taxi routes
@app.route('/taxi/release')
def handle_taxi_release():
  return ''

# Passenger routes
@app.route('/passenger/order/create')
	def handle_create_order():
		return ''

@app.route('/passenger/order/cancel')
	def handle_cancel_order():
		return ''