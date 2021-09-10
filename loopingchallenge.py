import os

os.system('cls')

star=int(input("How many stars? "))
print("stars", star)
line=star
for i in range(line):
    # i starts from 0 and stops looping on line-1
    for space_counter in range(i):
        print(" ", end= " ")
    for counter in range(star): # You can use a number or a variable
        print("*", end= " ")
        #print(counter, end=" ")
    print()
    star-=1
print("Thank you! ")