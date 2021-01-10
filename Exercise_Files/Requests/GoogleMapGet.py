import requests
import pprint
from requests.structures import CaseInsensitiveDict


import pprint
from requests.structures import CaseInsensitiveDict


url = "https://rahulshettyacademy.com/maps/api/place/get/json/?Key=qaclick123&place_id=4a81fa108119ae4e4a3ba1cc6c3bb770"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

resp = requests.get(url, headers=headers)
resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.text)


