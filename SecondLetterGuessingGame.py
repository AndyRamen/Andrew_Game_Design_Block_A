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
    print("You have to guess a word, the type of word is provided below")
    print()
    print("###############################")
    print("          ----Menu----         ")
    print(                                 )
    print("           1. Animals          ")
    print("           2. Computer Parts         ")
    print("           3. Fruits         ")
    print("           4. Scoreboard        ")
    print("           5. Exit          ")
    print()
    print("############################")
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

animals=["tiger", "elephant", "lion"]
fruits=["apple", "strawberry", "blueberry"]
compParts=["keyboard", "monitor", "case", "mouse"]
name= input("What is your name? ")
maxScore=0
sel = Menu()


while sel !=5:
    if sel == 1:
        print(name + ", good luck! You have 5 chances to guess my word.")
        word = random.choice(animals)
        word = word.lower()
        wordCount=len(word)
        turns=wordCount+2
        score=0
        letCount=0
        print(word) #Just for checking our code, remove later.
        guesses = '' 
        updateWord(word, guesses)

        while turns > 0 and letCount<wordCount:
            print()
            newguess=input("Give me a letter: ")
            newguess=newguess.lower()
            if newguess in word:
                guesses += newguess
                print("You guessed one letter. ")
            else:
                turns-=1
                print("Sorry, you have ", turns, " turns left.")
            updateWord(word, guesses)    
    if sel == 2:
        print(name + ", good luck! You have 5 chances to guess my word.")
        turns=5
        word = random.choice(compParts)
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
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
    myFile= open('score.txt', 'r')
    myFile.write("\n Score:", + maxScore)
    sel=Menu()