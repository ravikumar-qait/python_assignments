import os
import shutil 
from os import makedirs

my_list = []
my_list = os.listdir("/home/qainfotech/Desktop/ravi/new1")
size = len(my_list)
print("size is" , size)
k = int(input("Enter k "))
#cnt = 0
#for files in os.listdir("/home/qainfotech/Desktop/ravi/new1"):
 #   cnt = cnt+1
rem = size%k
if (rem!=0):
    folder_to_create = int((size/k)+1)
else:
    folder_to_create = int((size/k))
folder_path = []
print(folder_to_create)
for i in range(folder_to_create):
    x = input("give name of folder ")
    makedirs(x)
    folder_path.append(x)

#for i in range(len(folder_path)):
#    print(folder_path[i])
y = 0
for i in range(folder_to_create):
    for j in range(k):
        if(y<size):
            pth1 = '/home/qainfotech/Desktop/ravi/new1/'+my_list[y]
            source = pth1;
            y = y+1
            pth2 = '/home/qainfotech/Desktop/python/' + folder_path[i]
            destination = pth2
            shutil.move(source, destination)





