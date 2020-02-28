import requests
import string
ck = requests.get('http://10.0.10.198:8000/api/v1/challenges/6/')

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




















