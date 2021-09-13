#Andrew Cai
#09/13/21
#This is about data types
#How  strings work
#Integers: long (8 bytes), float (4 bytes), double (8 bytes), boolean
#Float uses decimal. If you put 5.0 instead of 5, it will think it's a float instead of a long.
#Boolean is true or false (binary).

import os

os.system('cls')
userInput=input("type something ")
print (type(userInput))
try:
    int(userInput)
    check=True
except ValueError:
    check=False

if(check):
    #I will be back
    print()
else:
    print(len(userInput))
for i in userInput:
    print(i)

if len(userInput>3):
    print (userInput[3])