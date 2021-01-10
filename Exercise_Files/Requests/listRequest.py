import requests
import pprint
import json
import jsonpath

from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
url ="https://regres.in/api/unknown"

response = requests.get(url)
print(response.status_code)