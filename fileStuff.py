#Andrew Cai
#10/7/2021
#We are going to learn how to write to a file, how to read to a file, how to append to a file, and how to close a file
import os, time
#To create a file you must declare an object so we can open a file.
#When you open a file you need to use 'w'
myFile= open('score.txt', 'w')
myFile.write("Hello there, my name is Andrew \t what is yours?")
myFile.close()
#Always close a file when you are done using it.
myFile= open('score.txt', 'w')
myFile.write("And now we will play a game")
myFile.close()
#Read and print the file
fileMy= open('score.txt', 'r')
print(fileMy.read())
fileMy.close()
score=450
anotherFile= open('score.txt', 'a')
anotherFile.write("\n The highest score: \t" + str(score))
anotherFile.close()