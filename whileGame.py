#learning while loop

#Control the main game
#Instructions of the game here
answer = input("Do you want to play a game? ")
while ('y' in answer):
    print("Welcome!")
    num = int(input("Give me a number: "))
    #Put try and except here, inside the while loop.
    while (num >10):
        print (num)
        num += 5
    print("THis is your number ", num)
    answer = input("Do you want to play again?")
    print("Thank you for playing! ")