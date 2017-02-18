import requests

def send_post(url, data):
	try:
		print(requests.post(url, data).text)
	except requests.exceptions.ConnectionError:
		print('Connection error. May be you forgot to start server?')
		exit()
	except requests.exceptions.RequestException as e:
		print('Error while trying to send POST %s', url)
		print(e)