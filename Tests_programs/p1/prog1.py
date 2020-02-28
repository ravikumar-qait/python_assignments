import requests
import string
import json
import urllib


url = 'http://10.0.10.198:8000/api/v1/challenges/1/?format=json'
username = 'ravikumar'
password = 'qainfotech'

r = requests.get(url, auth= (username,password))
page = r.json()

string_input = (page['sample_input']['text'])

count = 0
for i in string_input:
    if i.isalnum():
        count +=1

#print(count)

data1 =  {
    "candidate": 4,
    "challenge": 1
} 


url1 = 'http://10.0.10.198:8000/api/v1/testsessions/'
r = requests.post(url = url1 , data = data1 , auth = (username,password))

check_id = r.content
print(check_id)
url2 = 'http://localhost:8000/api/v1/testsessions/check_id/'
