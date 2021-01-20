import requests
import pprint
import time
from Exercise_Files.Requests.libs.openexchange import OpenExchangeClient

APP_ID="5aac0053c7684a2391b2cc541a45c764"
#client = OpenExchangeClient(APP_ID)
#https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID
#response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
#pprint.pprint(response.json())
#exchange_rates = response.json()["rates"]
#print(exchange_rates)

client = OpenExchangeClient(APP_ID)
usd_amount=1000
start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()
print(f"USD{usd_amount} is GBP{gbp_amount}")
print(end-start)



start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()
print(f"USD{usd_amount} is GBP{gbp_amount}")
print(end-start)


start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()
print(f"USD{usd_amount} is GBP{gbp_amount}")
print(end-start)