import requests

response = requests.get("https://freegeoip.app/json/").json()

for key in response:
	print("{key}: {value} ".format(key = key, value = response[key]))