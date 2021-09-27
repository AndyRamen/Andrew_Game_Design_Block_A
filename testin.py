import os
os.system('cls')

import random
print("I will choose one word and give you multiple hints. Try guessing. Type anything to continue.")
answer = input("Do you want to play? ")
userInput = answer
print("Guess the word! Guess either dog, fish, cat, snake, or rabbit.")
while ('y' in answer):
    start=1
    words= ["dog", "fish", "cat", "snake", "rabbit"]
    myword = random.choice(words)
    myword = myword.lower()



    
    print("New word!")
    print()
    while (start==1):
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