import requests
import pprint
import random
import math

randomVal =  math.floor(random.random() *10)


url = "https://reqres.in/api/users/"+str(randomVal)

print(url)

resp = requests.get(f"https://reqres.in/api/users/{randomVal}")
#print(resp.json())
respond = resp.json()

#print("********************\n")
pprint.pprint(respond)