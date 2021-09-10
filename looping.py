# Andrew Cai
# 09/07/21
# We are going to learn how to use a for loop
import os

os.system('cls')

star=int(input("How many stars? ")) #Input is always str
#Type casting changes type of data
print("stars", star)
line=star
for i in range(line):
    #Add a loop for the spaces here
    for counter in range(star): # You can use a number or a variable
        print("*", end=" ")
        #print(counter, end=" ")
    print()
    star-=1
# print a return creates a new line
print("Thank you! ")