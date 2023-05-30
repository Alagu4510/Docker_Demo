import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
json = response.json()
print(json)