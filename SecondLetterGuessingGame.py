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
    elif sel== 3:
        word= random.choice(fruits)

animals=["tiger", "elephant", "lion"]
fruits=["apple", "strawberry", "blueberry"]
compParts=["keyboard", "monitor", "case", "mouse"]
name= input("What is your name? ")
maxScore=100
sel = Menu()

def exit():
    myFile= open('score.txt', 'a')
    myFile.write(name + "\t Highest score:\t"+str(maxScore))
    #Line 103 and 104 should be put into exit funct.
    myFile.close()
    #Call exit function
    print("So long, " + name + "!")
    os._exit()

def gameOver():
    print("Game over!")
    sel=Menu()

def sel4():
    myFile= open('score.txt', 'r')
    print(myFile.read())
    myFile.close()
    #Turn into function and CLOSE FILE
    sel=Menu()
def wordSelection():
    if sel == 1:
        word = random.choice(animals)
    if sel == 2:
        word = random.choice(compParts)
    if sel == 3:
        word = random.choice(fruits)
    return word

if sel==5:
    exit
if sel ==4:
    sel4
while sel !=5 and sel !=4:
    word=wordSelection()
  
    word = word.lower()
    wordCount=len(word)
    turns=wordCount+2
    score=0
    print(name + ", good luck! You have", turns, "chances to guess my word.")
    print(word) #Just for checking our code, remove later.
    guesses = '' 
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
        updateWord(word, guesses)    
if turns==0:
    print("Sorry but you're out of turns!")
    answer=input("Return to menu? ")
    while ('y' in answer):
        sel=Menu()
    
       
        os.system('cls')
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)

    myFile= open('score.txt', 'r')
    myFile.close()
    sel=Menu()