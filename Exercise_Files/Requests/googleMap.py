import requests
import pprint
from requests.structures import CaseInsensitiveDict


url = "https://rahulshettyacademy.com//maps/api/place/add/json?&Key=qaclick123"
#headers = CaseInsensitiveDict()
#headers["Accept"] = "application/json"
#headers["Content-Type"] = "application/json"
#headers["Content-Length"]="calculated when request is sent"
#headers["Connection"]="keep-alive"


headers = { 'Content-Type' : 'application/json'}

data = {
  "location": {
    "lat": -38.383494,
    "lng": 33.427362
  },
  "accuracy": 50,
  "name": "Frontline house",
  "phone_number": "(+91) 983 893 3937",
  "address": "29, side layout, cohen 09",
  "types": [
    "shoe park",
    "shop"
  ],
  "website": "http://fastsnowboarder.com",
  "language": "French-IN"
}


resp = requests.post(url, headers=headers, data=data)
print(resp.status_code)
print(resp.content)
print(resp.text)

