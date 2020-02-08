week_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# ankitksr: Think about implementing this without maintaining two parallel data structures.
color_list = []
color_set = set()
# ankitksr: Try iterating directly over the 'list' iterable instead of a range function by calculating the list's length.
for i in range(len(week_list)):
    color = input("Enter Color for:" + week_list[i] + ":")
    color_list.append(color)
    color_set.add(color)

for i in range(len(color_list)):
    if color_list[i] in color_set:
        print(color_list[i], "color days are: ")
        count=0
        # ankitksr: See the above comments about looping.
        for j in range(len(color_list)):
            # ankitksr: The whole comparison login can be exponentially improved.
            if color_list[j] == color_list[i]:
                print(week_list[j])
                count= count+1
        color_set.remove(color_list[i])
        print(color_list[i] , "color total Count is: ",count)
