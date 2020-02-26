import string
import random
print("This program will generates a strong password \nPlease ensure that your password must have atleast 6 characters")
while 1:
    n = int(input("Enter the no of characters you want to include in your password:"))
    if n>=6:
        break
    else:
        print("please choose atleast 6 character long password")
        continue

password = ""
for i in range(n):
    password += ( ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation )) )

print (password)
