
import requests
from Exercise_Files.Requests.payloaddata.payloadtype2 import payloadtype

url = "http://httpbin.org/post"





#payload = "{\n    \"key1\": 1,\n    \"key2\": \"value2\"\n}"
#payload ={
 #         "key1":1,
  #        "key2": "value2"
  #       }

headers = {
    'Content-Type': "application/json,text/plain",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e908a437-88ea-4b00-af53-7a9a49033830,ba90e008-0f7f-4576-beb8-b7739c8961f1",
    'Host': "httpbin.org",
    'accept-encoding': "gzip, deflate",
    'content-length': "42",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payloadtype(), headers=headers)

print(response.status_code)
assert response.status_code == 200


print(response.text)

