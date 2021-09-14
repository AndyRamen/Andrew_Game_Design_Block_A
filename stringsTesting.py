import os

os.system('cls')
#I am just typing it out to see if it works then deleting it.

txt = "This is me doing my coding homework"
if "free" not in txt:
    print("Free isn't here.")

l = "Hello World!"
print(l[:4])

a = "This is my game design homework."
b = " Below is code I made myself."
c = a + b
print(c)

age = (input("Type your age: "))
txt = "My name is Joe, I am {}" 
print(txt.format(age))

quantity = 4
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

e = (input("Type out a sentence: "))
f = e
print(f[:4])
print("I forgor 💀")
f = e 
print(f[-5:-2])



