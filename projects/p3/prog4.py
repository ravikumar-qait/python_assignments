string_input = input()
my_dict = {'a': 0,'e':0,'i':0,'o':0,'u':0}
count = 0
for i in range(len(string_input)):
    char = string_input[i]
    if char in ('a','e','i','o','u'):

        my_dict[char]  += 1
    
for i in my_dict:
    print(i,my_dict[i])