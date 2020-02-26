import csv
import random

crimefile = open('words.txt', 'r')
reader = csv.reader(crimefile)
allRows = [x for x in reader]

my_list = []

for i in range(len(allRows)):
    my_list.append(allRows[i][0])

random_word = my_list[(random.randrange(0,len(my_list)))]

display_string = []
for i in range(len(random_word)):
    if random_word[i] in ['a','e','i','o','u']:
      display_string.append(random_word[i])
    else:
        display_string.append('_')
print("This is a word Game in which you have to guess the characters which may be in the word.\nFor you easiness Vowels are already placed on its place")
print("The word is: ",end ="")
for i in display_string:
    print(i,end=" ")

no_of_guesses = 10
i=0
flag = 0

while i < 10:
    chara = input("\nGuess Any random character which you think may be in word: ")
    if chara in random_word:
        for j in range(len(random_word)):
            if random_word[j] == chara:
                display_string[j] = chara
        for y in range(len(display_string)):
            if display_string[y] == '_':
                print("Correctly guessed, Now guess left ones. \nThe word is:  ",end="")
                break
            elif y == len(random_word)-1:
                print("Whooa! You Win :) The Word is",random_word)
                flag=1
                break
    elif i < 9:
        print("Incorrect Guess (: \nLife left:",(9-i)*'* ',"\nThe Word is:  ",end='')
        i = i+1
    else:
        print("OOPS! You Died(:  The word is: ",random_word)
        break
    if flag==1:
        break
    for k in display_string:
        print(k,end=" ")


