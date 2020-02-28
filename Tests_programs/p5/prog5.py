my_list = []

number = int(input())
my_set = set()
ans_list = []

for i in range(number):
    scan = int(input())
    my_list.append(scan)
    if scan not in my_set:
        ans_list.append(scan)
    my_set.add(scan)

print(ans_list)
