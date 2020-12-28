# Python Essential Libraries by Joe Marini course example
# Example file for the Requests library
import requests
from requests.auth import HTTPDigestAuth

# define user and password values
user = "theuser"
passwd = "thepass"

# TODO: use the basic authentication method

#url = "https://httpsbin.org/basic-auth/theuser/thepass"
#resp = requests.get(url, auth=(user,passwd))
#print(resp.status_code)
#print(resp.txt)




# TODO: use the digest authentication method
url = "https://httpsbin.org/basic-auth/theuser/thepass"
resp = requests.get(url,auth=HTTPDigestAuth(user,passwd))
print(resp.status_code)
print(resp.txt)
