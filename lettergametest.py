import random, os
os.system('cls')
#function to update dashes and letters
def updateWord(word, guesses, letCount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
    return letCount
#define function for Menu
def Menu():
    print("########################################")
   ## put instructions right above menu
    print("#                MENU                  #")
    print("#                                      #")
    print("#       1. Animals                     #")
    print("#       2. Computer PArts              #")
    print("#       3. Fruits                      #")
    print("#       4. ScoreBoard                  #")
    print("#       5. Exit                        #")
    print("#    To play the game select 1-4       #")
    print("#       To exit select 5               #")
    print("########################################")
    print()
    sel=input("What would you like to do? ")
    # add the Try and except before you force sel to be an int
    sel=int(sel)
    return sel
def selWord(sel):
    if sel == 1:
        word= random.choice(animals)
    elif sel ==2:
        word= random.choice(compParts)
    elif sel ==3: 
        word= random.choice(fruits)
    elif sel ==4:
        if sel ==4:
            myFile=open('score.txt', 'r')
            print(myFile.read)
            myFile.close()

    elif sel ==5:
        def exit():
            if sel==5:
                print("Bye!")
                os._exit()
    return word


# create the function for the score board and comeback to main menu
# create the function to Exit, where you write to the file the max score and exit game

animals=["tiger", "elephant"]
fruits=["banana", "strawberries"]
compParts=["keyboard", "Monitors", "computer","trackpad", "case","Operating System"]

name= input("What is your name? ")
maxScore=0 #to store highest Score
sel = Menu()
print(sel)
while sel==1 or sel==2 or sel==3:
    print(name, " Good Luck! you have 5 chances to guess")
    
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    turns= wordCount+2  #depending on the lenght if the word
    letCount=0 #variable to check if the user guessed the word
    print(word) # just for checking our code delete later
    guesses=''
    score=0
    letCount=updateWord(word, guesses, letCount)
    while turns > 0 and letCount<wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess
            
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        letCount=0
        letCount= updateWord(word, guesses, letCount)
    os.system('cls')
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
    sel=Menu()
if sel ==4:
    selWord(sel)