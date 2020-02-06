import os
import shutil 
from os import makedirs

files_list  = []
y=0

dir_path = os.path.dirname(os.path.realpath(__file__))

files_list = os.listdir(dir_path)
total_files = len(files_list)

print("Total no of files are: " ,total_files )

folder_to_divide = int(input("Enter the no of folders your want to divide into:"))

remainder = total_files%folder_to_divide
if (remainder!=0):
    folder_to_create = int((total_files/folder_to_divide)+1)
else:
    folder_to_create = int((total_files/folder_to_divide))
folder_list = []

for i in range(folder_to_create):
    folder_name = input("Give name of folder:")
    folder_path = dir_path +'/'+ folder_name
    os.mkdir(folder_path)
    folder_list.append(folder_name)


for i in range(folder_to_create):
    for j in range(folder_to_divide):
        if(y<total_files):
            source_path = dir_path +'/'+files_list[y]
            source = source_path
            destination_path = dir_path +'/'+ folder_list[i]
            destination = destination_path
            shutil.move(source_path, destination_path)
            y = y+1


print("Successfully Moved!")










