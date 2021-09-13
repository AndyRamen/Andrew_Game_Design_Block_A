import os
os.system('cls')

num= int(input("Give me a number "))
digit1 = num%10
print("Your last digit is:", digit1)

digit2 = num%100
print("Your second digit is:", digit2)

digit3 = num%1000
print("Your third digit is:", digit3)

digit4 = num%10000
print("Your fourth digit is:", digit4)

digit5 = num%100000
print("Your fifth digit is:", digit5)