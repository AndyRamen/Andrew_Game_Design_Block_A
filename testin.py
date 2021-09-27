import os
os.system('cls')

import random
print("I will choose one word out of 5. Try guessing. Type 'yes' to continue")
answer = input("Do you want to play? ")
userInput = answer
print("Guess the word! Guess either dog, fish, cat, snake, or rabbit.")
while ('y' in answer):
    tries=5
    start=1
    words= ["dog", "fish", "cat", "snake", "rabbit"]
    myword = random.choice(words)
    myword = myword.lower()



    
    print("New word!")
    print()
    while (start>0):
        userInput= input("What is your guess? ")
        userInput=userInput.lower()
        if userInput== myword:
            print("Correct! ")
            print()
            start=0
        else:
            userInput != myword
            print("Incorrect. Try again.")
            print()
            tries-=1
            print(tries)
    if tries==0:
        print("You're out of tries!")
        break