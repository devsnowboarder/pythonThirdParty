import requests
import pprint
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
  "Id": 78912,
  "Quantity": 1,
  "Price": 18.00
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print(resp.json())


###################################

url = "https://api.exchangeratesapi.io/latest?base=USD"


resp = requests.get(url)

print(resp.status_code)
print(resp.json())
pprint.pprint(resp.json())