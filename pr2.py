week_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
color_list = []
color_set = set()
for i in range(len(week_list)):
    color = input("Enter Color for:" + week_list[i] + ":")
    color_list.append(color)
    color_set.add(color)

for i in range(len(color_list)):
    if color_list[i] in color_set:
        print(color_list[i], "color days are: ")
        count=0
        for j in range(len(color_list)):
            if color_list[j] == color_list[i]:
                print(week_list[j])
                count= count+1
        color_set.remove(color_list[i])
        print(color_list[i] , "color total Count is: ",count)
