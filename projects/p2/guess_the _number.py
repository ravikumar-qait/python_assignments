import random
print("This is a Guessing no. game in which you have to guess a number between 1 and 100 \nYou are provided a maximum of 5 guesses to guess the element")

real_number = random.randrange(1,100)
total_guesses = 5

for i in range(total_guesses):
    guess = int(input("Guess the number:"))
    if guess == real_number:
        print("Whooa! You find It")
        break
    elif guess < real_number:
        if i <= total_guesses-2:
             print("OOPS! Your Guessed number is smaller than the original, You can try again guessing a greater number")
             print("Tries Left",total_guesses-1-i)
        else:
            print("OOPS! You Failed, Better Luck next time")
            break
    else:
        if i <= total_guesses-2:
            print("OOPS! Your Guessed number is greater than the original, You can try again guessing a smaller number")
            print("Tries Left",total_guesses-1-i)
        else:
            print("OOPS! You Failed, Better Luck next time")
            break
    