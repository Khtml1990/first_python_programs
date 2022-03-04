# import neccessary modules
import random

# Welcome prompts
print("\nWelcome to the quiz")


playing = input("Would you like to play Guess the Number? ")

# If user doesn't enter yes, quit the program, otherwise, continue.
if playing.lower() !="yes":
    print("Maybe next time. Goodbye")
    quit()  

# Promt user for their name and store it
name = input("Great! What should we call you? ")

print("\nHere's how the game is played \nGuess what number I'm think of between a range of numbers that you determine\nFor each guess, I'll tell you if you're too high, or too low until you guess the right number!\n")
print("Good luck "+ name +"!\n")

# Get range
low_num = int(input("What number should the range start at? "))
high_num = int(input("What number should the range end at? "))

# Ensure that the start of the range is lower than end of range.
while low_num>high_num:
    print("Start of range must be a lower number than the end of range!")
    low_num = int(input("What number should the range start at? "))
    high_num = int(input("What number should the range end at? "))

# Get random number based on user's range
random_num = random.randint(low_num,high_num)

# Keep track of how many attempts there are
attempts = 0



while True:
    guess = input("Make your guess ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("You should only be guessing numbers")

    if guess<random_num:
        attempts+=1
        print("You're too LOW")
        continue
    elif guess>random_num:
        attempts+=1
        print("You're too HIGH")
        continue
    else:
        print("Good job!")
        print("You guessed the right number was "+ str(random_num)+ ", and it took you "+str(attempts)+" tries!")
        break