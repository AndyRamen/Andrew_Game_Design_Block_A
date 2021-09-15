import os

os.system('cls')

userInput=input("type something: ")
print (type(userInput))
try:
    int(userInput)
    check=True
except ValueError:
    check=False
if(check):
    print()
else:
    print(len(userInput))

var1=int(input("Type your first number: "))
var2=int(input("Type your second number: "))
print("Note: In subtraction the second number will be subtracted from the first. In division, it will be the first number divided by the second.")

print()
addanswer = var1+var2
print("Addition answer:", addanswer)
print()
subtanswer = var1-var2
print("Subtraction answer:", subtanswer)
print()
multanswer = var1*var2
print("Multiplication answer:", multanswer)
print()
divanswer = var1/var2
print("Division answer:", divanswer)
print()
modanswer = var1%var2
print("Modulus answer:", modanswer)
print("The modulus tells you the remainder between the two numbers.")
print()
