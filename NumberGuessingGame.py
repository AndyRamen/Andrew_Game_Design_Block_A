# Andrew Cai
# 09/15/21
#if(random number-guess>25)
# print("Too high!")

import os
os.system('cls')

import random

answer = input("Do you want to play a game? Y/N ")
check = False

while ('y' in answer):
    guessesTaken = 0
    number = random.randint(1, 50)
    print(number)
    print("I am thinking of a number between 1 and 50. You have 6 chances to guess it. ")

    while guessesTaken < 6:
        print("Take a guess: ")
        guess = input()
        try:
            guess = int(guess)
            check = True
        except ValueError:
            print("Put an actual integer! ")
            print()
            check = False
        if check == True:
            guessesTaken += 1
            if guess < number:
                print("Your guess is too low! Try again.")
                print()
            
            if guess > number:
                print("Your guess is too high! Try again.")
                print()

            if guess == number:
                guessesTaken = str(guessesTaken)
                print("Great job! You guessed my number in " + guessesTaken + " guesses!")
                print()
            answer=input("Do you want to play again? Y/N: ")
            break

        if guessesTaken > 6:
            number = str(number)
            print("Sorry but you've reached your guess limit. The number I was thinking of was " + number)
            print()  
        answer=input("Do you want to play again? Y/N: ")

if guess == number:
    input("Play again? ")
    print()

if guess != number:
    input("Play again? ")
    print()


