import requests
url_api = 'https://api.midway.tomtom.com/ranking/liveHourly/USA_los-angeles'
us_req = requests.get(url_api)
us_json = us_req.json()

print(us_json)
