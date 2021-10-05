#Word Game
# We are creating a list of words
# Randomly select a word from the list for the user to guess.
# Use has a limited amount of turns
# Swhor the word to the user with the characters in spaces.
# Play as long as the user has turns or hasn't guessed the word.


import random, os
os.system('cls')

def updateWord(word, guesses): #Function to update dashes
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end= " ")
#define function for menu
def Menu():
    print()
    #Add instrpuctions here
    print("          ----Menu----         ")
    print(                                 )
    print("           1. Animals          ")
    print("           2. Computer parts         ")
    print("           3. Fruits         ")
    print("           4. Exit          ")
    print("To play the game, select 1-3 and to exit select 4.")
    print()
    sel=input("What would you like to do? ")
    #Put in try and except here
    sel=int(sel)
    return sel

def selWord():
    if sel == 1:
        word= random.choice(animals)
    elif sel == 2:
        word= random.choice(compParts)
    else:
        word= random.choice(fruits)

animals=["dog", "tiger", "elephant", "lion"]
fruits=["apple", "strawberry", "blueberry", "pear"]
compParts=["keyboard", "monitor", "case", "mouse", "trackpad"]
name= input("What is your name? ")
counter=0
sel = Menu()
if sel ==4:
    print("Bye, " + name + "!")

while sel !=4:
    if sel == 2:
        print(name + ", good luck! You have 5 chances to guess my word.")
        turns=5
        counter +=1
        word = random.choice(compParts)
        word = word.lower()
        print(word) #Just for checking our code, remove later.
        guesses = ' ' 
        updateWord(word, guesses)

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
    
    if sel == 1:
        print(name + ", good luck! You have 5 chances to guess my word.")
        turns=5
        counter +=1
        word = random.choice(animals)
        word = word.lower()
        print(word)
        guesses = ' ' 
        updateWord(word, guesses)

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

    if sel == 3:
        print(name + ", good luck! You have 5 chances to guess my word.")
        turns=5
        counter +=1
        word = random.choice(fruits)
        word = word.lower()
        print(word) 
        guesses = ' ' 
        updateWord(word, guesses)

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
    updateWord(word,guesses)
             

    os.system('cls')
    sel=Menu()