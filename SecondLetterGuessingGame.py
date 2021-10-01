#Word Game
# We are creating a list of words
# Randomly select a word from the list for the user to guess.
# Use has a limited amount of turns
# Swhor the word to the user with the characters in spaces.
# PLay as long as the user has turns or hasn't guessed the word.

import random, os
os.system('cls')

compParts=["keyboard", "Monitors", "computer", "mouse", "case", "operating system"]
print("Word Game ")
print(" Guess what computer part I am thinking of. ")
name= input("What is your name? ")
counter=0
answer = input( name + ", do you want to play? ")
while ('y' in answer):
    print(name + ", good luck! You have 5 chances to guess my word.")
    turns=5
    counter +=1
    word = random.choice(compParts)
    word = word.lower()
    print(word) #Just for checking our code, remove later.
    guesses = ' ' 
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end=' ')
    while turns > 0:
        print()
        newguess=input("Give me a letter: ")
        newguess=newguess.lower()
        if newguess in word:
            guesses += newguess
            print("You guessed one letter. ")
        else:
            turns-=1
            print("Sorry, you have ", turns, " turns left.")
        
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print('_', end= " ")
    answer=input(name + " Do you want to play again?")