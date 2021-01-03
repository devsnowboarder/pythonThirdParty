import requests
import pprint
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/photos'

#get the data about the photos
response = requests.get(url)

#read that data into a variable
json_data = response.json()


#print(json_data)
pprint.pprint((json_data))



url_list = []
for photo in json_data:
    url_list.append(photo['url'])

title_list=[]
for title in json_data:
    title_list.append(title['title'])

albumId_list=[]
for album in json_data:
    albumId_list.append(album['albumId'])

for album in albumId_list:
    print(album)

for url in url_list:
    print(url)

for title in title_list:
    if 'tempora quia dignissimos et est aut et' in title:
      print("found the title " + title)


print(len(url_list))

#How many items are there if we turn that list into a set?
print(len(set(url_list)))


output ='photo.csv'
f= pd.DataFrame(title_list)
#print(df.head())
#df.to_csv(output,index=False)


