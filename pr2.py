week_dict = {"Monday":"","Tuesday":"","Wednesday":"","Thursday":"","Friday":"","Saturday":"","Sunday":""}
color_set = set()

for i in week_dict:
    color = input("Enter Color for " + i + ":")
    week_dict[i] = color
    color_set.add(color)

for i in week_dict:
    if week_dict[i] in color_set:
        print(week_dict[i], "color days are: ")
        count=0
        print(list(week_dict.keys())[list(week_dict.values()).index(week_dict[i])])
        color_set.remove(week_dict[i])
         
# print(week_dict[i] , "color total Count is: ",count)