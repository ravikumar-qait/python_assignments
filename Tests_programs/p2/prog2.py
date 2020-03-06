string_input = input()
count = 0
for i in range(len(string_input)):
    char = string_input[i]
    if char == ' ' and  string_input[i+1] != ' ':
        count+=1

print(count)
