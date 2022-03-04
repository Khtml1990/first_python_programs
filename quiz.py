# Welcome prompts
print("\nWelcome to the quiz")


playing = input("Would you like to attempt the Dev Quiz? ")

# If user doesn't enter yes, quit the program, otherwise, continue.
if playing.lower() !="yes":
    print("Maybe next time. Goodbye")
    quit()  

# Promt user for their name and store it
name = input("Great! What should we call you? ")

print("\nHere's how the game is played \nI'll display questions, and you'll answer them.\nTry to answer all 5 correct\n")
print("Good luck "+ name +"!\n")

# Variables to keep track of correct answers
correct = 0

# Question 1
answer = input("\nWhat programming language uses the file extension 'py'? ")

if answer.lower() == "python":
    correct+=1
    print("Correct!")
else:
    print("Incorrect")

# Question 2
answer = input("\nWhat does 'JS' stand for? ")

if answer.lower() == "javascript":
    correct+=1
    print("Correct!")
else:
    print("Incorrect")

# Question 3
answer = input("\nTrue or false? Java is a dynamically-typed language:  ")

if answer.lower() == "false":
    correct+=1
    print("Correct!")
else:
    print("Incorrect")

# Question 4
answer = input("\nWhen was JavaScript invented? ")

if answer == "1995":
    correct+=1
    print("Correct!")
else:
    print("Incorrect")


# Question 5
answer = input("\nTrue or false? This was a good quiz: ")

if answer.lower() == "true":
    correct+=1
    print("Correct!")
else:
    print("Incorrect")

print("\nYou got "+str(correct)+" out of 5 right",end="")

if correct==5:
    print("!\nYou got " + str(int(correct/5*100)) + "%")
elif correct >3:
    print("!\nYou got " + str(int(correct/5*100)) + "%")
elif correct==0:
    print(".\nHit the books\nYou got " + str(int(correct/5*100)) + "%")
else:
    print(".\nCould be better\nYou got " + str(int(correct/5*100)) + "%")