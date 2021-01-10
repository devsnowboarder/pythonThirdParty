import json

import requests
import pprint
import jsonpath


from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
#headers["Content-Type"] = "application/json"

url ="https://regres.in/api/users?page2=2"


response = requests.get(url,headers=headers)
print(response.status_code)
#json_response = json.loads(response.content)
#print(json_response)
print(response.text)


url ="https://reqres.in/api/users/2"
response = requests.get(url,headers=headers)
print(response.status_code)

json_response =json.loads(response.text)





url ="https://reqres.in/api/unknown/2"
response = requests.get(url,headers=headers)
print(response.status_code)

print(response.text)
print(response.json())
json_response =json.loads(response.text)
pprint.pprint(response.json())

pages = jsonpath.jsonpath(json_response,"data.id")
print(pages)
pages = jsonpath.jsonpath(json_response,"data.name")
print(pages)
assert pages == ['fuchsia rose']

pprint.pprint(response.json())