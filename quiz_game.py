
print("Welcome to my quiz game")

playing = input("Do you want to play a game? ")

if playing.lower() == "no":
    quit()
print("be aware that spelling is important!")

ready = input("Are you ready? ")

if ready.lower() == "yes":
    print("Ok let's play the game :) ")   
    
score = 0

answer = input("Where is apple headquarter? ")
if answer.lower() == "usa":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


answer = input("What is CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


answer = input("Where is GPU? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


answer = input("What is RAM? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("Well done! you got " + str(score) + " questions correct.")

