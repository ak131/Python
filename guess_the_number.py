print("Please think of a number between 0 and 100!")

low=0
middle=50
high=100

guess=raw_input("Is your number " + str(middle) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while guess != "c":
    if guess == "l":
        low=middle
        middle=int((middle+high)/2)
        guess=raw_input("Is your number " + str(middle) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif guess == "h":
        high=middle
        middle=int((middle+low)/2)
        guess=raw_input("Is your number " + str(middle) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    else:
        print("Please enter l, h, or c.")
        guess=raw_input("Is your number " + str(middle) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game Over. Your secret number was " + str(middle))