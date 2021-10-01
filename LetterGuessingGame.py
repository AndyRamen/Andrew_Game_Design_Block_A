import random


tup1 = ('holiday', 'active', '', 'letter', 'people', 'donate')
random_word = random.choice(tup1)
count = 0
print(random_word)
for x in random_word:
    print("_", end = " ")

while True:
    guess = str(input("Guess a letter:  "))
    guess = guess.lower()


    if (guess in random_word[0]):             
        print("Yay, its in the word")
        x-1

      
    
    else:                          
        count += 1
        print("Not in the word, attempts: %d" % count)
        
        if count > 5:                   
            print("You have reached max attempts")
            print("Sorry, but hangman died! You lose")
            break
        else:
            continue
    
    guess = str(input("Guess a letter: "))
    guess = guess.lower()

    if (guess in random_word[1]):
        print("Yay, its in the word")

    else:                          
        count += 1
        print("It's either not in the word, or its not in the correct space. Attempts: %d" % count)
        
        if count > 5:                   
            print("You have reached max attempts")
            print("Sorry, but hangman died! You lose")
            break
        else:
            continue