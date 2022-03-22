import requests
import pprint
import jsonpath
import json
import pandas as pd


api_key='39cbcf567177dbc06a77585a52cfba1d'
api_key_v4='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOWNiY2Y1NjcxNzdkYmMwNmE3NzU4NWE1MmNmYmExZCIsInN1YiI6IjVmZWNlM2EwNGNjYzUwMDAzYzdmNTNjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ED0IOavDxaRLBaT1Zj3fa5SyHrOSPgLnfRJjb7SHMJM'



#http requests
"""
GET -> grap data
Post -> add/update data


"""

#what are endpoint ( or a url )

#what is the http method what we need


"""

"""
#endpoint
#GET/movie/{movie_id}
#https://api.themoviedb.org/3/movie/550?api_key=39cbcf567177dbc06a77585a52cfba1d
"""
#movie_id=500
#api_version=3
#api_base_url =f"https://api.themoviedb.org/{api_version}"
#endpoint_path ="/movie/{movie_id}"
#endpoint = "{api_base_url}{endpoint_path}?api_key={api_key}"
#print(endpoint)
#resp=requests.get(endpoint)
##resp=requests.get(endpoint, json={"api_key":api_key)
#print(resp.status_code)
#print(resp.text)
"""

#using V4

#movie_id=501
#api_version=4

#api_base_url =f"https://api.themoviedb.org/{api_version}"
#endpoint_path =f"/movie/{movie_id}"
#endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key_v4}"
#print(endpoint)
#headers={
#    'Authorization': f'Bearer {api_key_v4}',
#    'Content-Type': 'application/json;charset=utf-8'
#}
#resp=requests.get(endpoint,headers=headers)
#resp=requests.get(endpoint, json={"api_key":api_key)
#print(resp.status_code)
#print(resp.text)




movie_id=500
api_version=3

searchQuery = 'The Matrix'
api_base_url =f"https://api.themoviedb.org/{api_version}"
endpoint_path =f"/search/movie"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searchQuery}"
print(endpoint)
resp=requests.get(endpoint)


print(resp.status_code)
print(resp.text)
print(resp.json())
pprint.pprint(endpoint)
pprint.pprint(resp.json())


json_response =json.loads(resp.text)
print("XXXXXXXXX")
pages = jsonpath.jsonpath(json_response,"results[0].id")
print(pages)
pages = jsonpath.jsonpath(json_response,"results[1].original_title")
print(pages)
print("XXXXXXXXX")




if resp.status_code in range(200,299):
    data =resp.json()
  #  print(data.keys())
    results = data['results']
  #  print(results[0].keys())
    movie_ids=set()
    for result in results:
        _id = result['id']
        print(result['title'],_id)
        movie_ids.add(_id)
   # print(list(movie_ids))

output = 'movies.csv'
movie_data =[]


for movie_id in movie_ids:
    api_version = 3
    api_base_url =f"https://api.themoviedb.org/{api_version}"
    endpoint_path =f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    resp = requests.get(endpoint)
    data = resp.json()
    movie_data.append(data)
    print(resp.json())


#df= pd.DataFrame(movie_data)
#print(df.head())
#df.to_csv(output,index=False)

