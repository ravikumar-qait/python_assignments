<<<<<<< HEAD
week_dict = {"Monday":"","Tuesday":"","Wednesday":"","Thursday":"","Friday":"","Saturday":"","Sunday":""}
color_set = set()

for i in week_dict:
    color = input("Enter Color for " + i + ":")
    week_dict[i] = color
=======
week_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# ankitksr: Think about implementing this without maintaining two parallel data structures.
color_list = []
color_set = set()
# ankitksr: Try iterating directly over the 'list' iterable instead of a range function by calculating the list's length.
for i in range(len(week_list)):
    color = input("Enter Color for:" + week_list[i] + ":")
    color_list.append(color)
>>>>>>> f6885194f9174ba3dd144287744f259b0f910848
    color_set.add(color)

for i in week_dict:
    if week_dict[i] in color_set:
        print(week_dict[i], "color days are: ")
        count=0
<<<<<<< HEAD
        for day,j in week_dict.items():
            if j == week_dict[i]:
                print (day)
=======
        # ankitksr: See the above comments about looping.
        for j in range(len(color_list)):
            # ankitksr: The whole comparison login can be exponentially improved.
            if color_list[j] == color_list[i]:
                print(week_list[j])
>>>>>>> f6885194f9174ba3dd144287744f259b0f910848
                count= count+1
        color_set.remove(week_dict[i])
        print(week_dict[i] , "color total Count is: ",count)
