import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint for retrieving exchange rates
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Send a GET request to the API
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        exchange_rate = data["rates"][to_currency]

