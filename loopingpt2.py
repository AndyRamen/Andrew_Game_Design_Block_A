import os

os.system('cls')

stars = int(input("Enter number of stars: "))
stars2 = stars
line = stars
space = 0

for i in range(line):
    for counter in range(stars):
        print("* ", end = " ")
    stars-=1
    
    for k in range(space):
        print("  ", end = " ")
    space +=2

    for counter in range(stars2):
        print("* ", end = " ")

    print()
    stars2-=1

print("Thanks!")
