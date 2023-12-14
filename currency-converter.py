import requests

API_KEY = 'fca_live_3SJypqaMnnilmbicuVZZcX9SXndF7we8Lq6bmOsC'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        return data["data"]
    except Exception as e:
        print("Invalid currency.")
        return None
    
while True:
    
    base = input("Enter the base curreny (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")