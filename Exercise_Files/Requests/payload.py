import requests

payload = {'name': 'Anthony', 'job': 'Programmer'}
resp = requests.post("https://reqres.in/api/users",json=payload)
print(resp.status_code)
print(resp.text)
