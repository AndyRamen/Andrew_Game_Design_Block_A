# Andrew Cai
# 09/15/21
#if(random number-guess>25)
# print("Too high!")

import os
os.system('cls')

import random

guessesTaken = 0
number = random.randint(1, 50)
print("I am thinking of a number between 1 and 50. Try to guess my number. You have a limit of 6 guesses. ")

while guessesTaken < 6:
    print("Take a guess. ")
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low! Try again.")
        print()
    
    if guess > number:
        print("Your guess is too high! Try again.")
        print()
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Great job! You guessed my number in " + guessesTaken + " guesses!")
    print()

if guess != number:
    number = str(number)
    print("Sorry but you've reached your guess limit. The number I was thinking of was " + number)
    print()


