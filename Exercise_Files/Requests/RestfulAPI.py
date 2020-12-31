import requests
import pprint

payload={'key1':'value'}

url ='https://httpbin.org/headers'


def responseCode(resp ):
    print(resp.status_code)

resp = requests.get(url,params=payload)

responseCode(resp)
print(resp.json())
pprint.pprint(resp.json())



response = requests.get("https://alexnormand-dino-ipsum.p.rapidapi.com/?format=text&words=10&paragraphs=1",
  headers={
    "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
    "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  }
)

print(resp.status_code)
print(resp.json())
pprint.pprint(resp.json())



