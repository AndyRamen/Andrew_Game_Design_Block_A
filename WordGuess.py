import os
os.system('cls')

import random
print("I will choose one word and give you multiple hints. Try guessing. Type anything to continue.")
words = ['cookie', 'rainbow', 'code', 'drums']
word = random.choice(words)
answer = input()
print(word)

print("Guess the word! I will give you a few hints.")

if word =='code':
    print("Hint: This is what I did to make this program!")
    input("What is your guess? ")
    if answer == 'code':
        print(answer.lower)
        print("Correct! ")
    if answer != 'code':
        print("That is not the answer! Here is another hint: ")
        print("Python is a type of this term.")
if word =='cookie':
    print("Hint: This is edible.")
    input("What is your guess? ")
    if answer == 'cookie':
        print(answer.lower)
        print("Correct! ")
    else:
        print("That is not the answer! Here is another hint: ")
        print("It comes in a chocolate chip flavor.")
if word =='rainbow':
    print("Hint: This is what shows up after a rainstorm!")
    input("What is your guess? ")
    if answer == 'rainbow':
        print(answer.lower)
        print("Correct! ")
    if answer != 'rainbow':
        print("That is not the answer! Here is another hint: ")
        print("It has a lot of colors.")
if word =='drums':
    print("Hint: A percussion instrument, it comes in a set.")
    input("What is your guess? ")
    if answer == 'code':
        print(answer.lower)
        print("Correct! ")
    if answer != ' code':
        print("That is not the answer! Here is another hint: ")
        print("A set of this includes cymbals.")
