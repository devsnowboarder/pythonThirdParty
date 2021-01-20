import requests
import pprint
from requests.structures import CaseInsensitiveDict
from Exercise_Files.Requests.baseURLs.httpbin import googleMap


import pprint
from requests.structures import CaseInsensitiveDict



headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

resp = requests.get(googleMap(), headers=headers)

print(resp.status_code)
pprint.pprint(resp.json())
print(resp.text)


