import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint for retrieving exchange rates
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Send a GET request to the API
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        exchange_rates = data["rates"]
        exchange_rate = exchange_rates[to_currency]

        converted_amount = amount * exchange_rate

        return converted_amount
    else:
        # If the API request fails, print an error message
        print("Unable to retrieve exchange rates.")
        return None
    
# Example usage
amount = 100  # Amount to convert
from_currency = "USD"  # Currency to convert from
to_currency = "EUR"  # Currency to convert to

converted_amount = convert_currency(amount, from_currency, to_currency)
if converted_amount is not None:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")

