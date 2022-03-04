# Importing modules
import random

# Welcome prompts
print("\nWelcome to the quiz")


playing = input("Would you like to play Rock Paper Scissors? ")

# If user doesn't enter yes, quit the program, otherwise, continue.
if playing.lower() !="yes":
    print("Maybe next time. Goodbye")
    quit()

# Promt user for their name and store it
name = input("Great! What should we call you? ")


print("Good luck "+ name +"!\n")

computer_score = 0
user_score = 0

valid_inputs = ["rock","paper","scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors (or 'Q' to quit): ").lower()
    if user_input == "q":
        break
    if user_input not in valid_inputs:
        print("Invalid input")
        continue

    random_number = random.randint(0,2)

    computer_pick = valid_inputs[random_number]

    print("\nComputer chose "+computer_pick+".")
    if user_input == computer_pick:
        print("It's a draw!")
    elif user_input == "rock" and computer_pick=="scissors":
        print("YOU WIN")
        user_score +=1
        
    elif user_input == "paper" and computer_pick=="rock":
        print("YOU WIN")
        user_score +=1
        
    elif user_input == "scissors" and computer_pick=="paper":
        print("YOU WIN")
        user_score +=1
    else:
        print("YOU LOST")
        computer_score+=1
        
print("\n" + name + ": "+str(user_score))
print("Computer: "+str(computer_score))
print("\nGoodbye!")