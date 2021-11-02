#Word Game
# We are creating a list of words
# Randomly select a word from the list for the user to guess.
# Use has a limited amount of turns
# Swhor the word to the user with the characters in spaces.
# Play as long as the user has turns or hasn't guessed the word.


import random, os
os.system('cls')

def updateWord(word, guesses): #Function to update dashes
    correctCount = 0
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
            correctCount += 1
        else:
            print('_', end= " ")
    if correctCount == len(word):
        return True
    else:
        return False

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
    print("To play the game, select 1-3 and to exit select 5.")
    print()
    sel=input("What would you like to do? ")
    #Put in try and except here
    sel=int(sel)
    return sel

def updateScoreFile():
    myFile= open('score.txt', 'a')
    myFile.write(name + "\t Highest score:\t"+ str(maxScore) + "\n")
    myFile.close()
    #Updates scoreboard file

def endGame():
    updateScoreFile()
    #print("So long, " + name + "!")
    print("So long,", name, "!")
    os._exit(0)
    #Ends game

def sel4():
    myFile= open('score.txt', 'r')
    print(myFile.read())
    myFile.close()
    sel = Menu()
    return sel
    #Opens and prints scoreboard

def wordSelection():
    if sel == 1:
        word = random.choice(animals)
    if sel == 2:
        word = random.choice(compParts)
    if sel == 3:
        word = random.choice(fruits)
    return word
    #Selects which category the word is going to be in.

animals=["tiger", "elephant", "lion"]
fruits=["apple", "strawberry", "blueberry"]
for i in range(0, len(animals)):
    fruits.append(animals[i])
print(fruits)


compParts=["keyboard", "monitor", "case", "mouse"]
name= input("What is your name? ")
maxScore = 0
#Words in category
#Main program starts here

sel = Menu()

while sel!=0:

    if sel==5:
        endGame()
    elif sel==4:
        sel = sel4()
    elif sel==1 or sel==2 or sel==3:
        word = wordSelection()
        word = word.lower()
        wordCount = len(word)
        turns = wordCount+2
        score = 0
        print(name + ", good luck! You have", turns, "chances to guess my word.")
        print(word) #Just for checking our code, remove later.
        guesses = '' 
        correctGuess = False
        updateWord(word, guesses)
        while correctGuess== False and turns > 0:
            print()
            newguess=input("Give me a letter: ")
            newguess= newguess.lower()
            if newguess in word:
                guesses += newguess
                print("You guessed one letter. ")
            else:
                turns -= 1
                print("\nSorry, you have ", turns, " turns left.")
            correctGuess = updateWord(word, guesses) 
        
        if correctGuess == False:
            print("Sorry but you're out of turns!")
        
        score = 3*wordCount + 5*turns
        if score > maxScore:
            maxScore = score
        answer = input("Return to menu? y/n ")
        if ('y' in answer):
            sel = Menu()
        else:
            sel = 0
    else:
        endGame()

endGame()
