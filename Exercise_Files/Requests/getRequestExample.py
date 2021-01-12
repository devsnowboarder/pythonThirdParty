import requests
import json
import jsonpath
import pprint

url ="http://jsonplaceholder.typicode.com/photos"


response = requests.get(url)
print(response.text)
print(response.status_code)
print(response.json())

pprint.pprint(response.json())


jsonPayload ={'albumId':1,
              'title':'test',
              'url':'nothing.com',
              'thumbnailUrl':'nothing.com'}

response = requests.post(url,json=jsonPayload)
print(response.status_code)
print(response.json())


url ="http://jsonplaceholder.typicode.com/photos"


response = requests.get(url)
print(response.text)
print(response.status_code)
print(response.json())

pprint.pprint(response.json())

json_data=response.json()
url_list=[]

for photo in json_data:
    url_list.append(photo['url'])

print(len(url_list))
print(len(set(url_list)))



