# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests
import pprint
from Exercise_Files.Requests.baseURLs.httpbin import responeBIN




# TODO: work with status codes
#resp = requests.get("https://httpbin.org/status/404")
#print(resp.status_code)
#resp.raise_for_status()

# TODO: examine response encoding

#resp = requests.get("https://httpbin.org/html")
#print(resp.encoding)
#print(resp.text)
#print(resp.content)

# TODO: To read JSON content, use the json() function

resp = requests.get(responeBIN())
#print(resp.json())
pprint.pprint(resp.json())
print(resp.headers)
print(resp.headers['content-type'])
respon=resp.json()
"""
for key, value in respon.items():
    print(key)
    for k,v in value.items():
        print(k,v)
"""


print(respon["slideshow"]["date"])
print(respon["slideshow"]["slides"][0])
print(respon["slideshow"]["slides"][1])

