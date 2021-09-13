#Andrew Cai
#Arithmetic operators
# + - * / %
# % is more important in comp sci
# % is mod
# Check for even numbers

import os
os.system('cls')

num= int(input("Give me a number: "))
rem=num%2
#conditional
if(rem ==0):
    print(" The number is even.")
else:
    print("The number is odd.")