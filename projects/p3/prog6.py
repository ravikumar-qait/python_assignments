
import requests
import string
ck = requests.get('http://10.0.10.198:8000/api/v1/challenges/1/')

print(ck.json())

a,b = input().split()
a = int(a)
b = int(b)

my_list = [True] * (b)

my_list[0] = False
my_list[1] = False
i = 2
for i in range(b):
    if my_list[i] == True:
        for j in range(2*i,b, i):
            my_list[j] = False

ans_list = []

for i in range(a+1,b):
    if my_list[i] == True:
        ans_list.append(i)

print(ans_list)


# {
#     'name': 'ravi kumar',
#     'id':1,
#     'marks': 45
# }

# HTTP Status: 
# HTTP headers:
# 'content_type': 'application/json'
# 'Authorization': 'hfjkbhkhbckjghwbgkj67487ngb'
# Http methods:
# GET -- get resource -- query_string ... www.ofg.com/?id=1&&name="ravi"
# POST -- params: {'name_initial': 'r'}
# PUT -- idempotent -- 
# PATCH -- {}
# OPTIONS --  


# cURL

# response = requests.get(url, params), requests.post
# response.status 
# response.text
# s = response.json()
