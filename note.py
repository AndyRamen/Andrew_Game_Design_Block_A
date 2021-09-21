#How to identify whether a integer or not.
#Note: Identify UserInput first.
try:
    userInput=int(userInput)
    check=True
except ValueError:
    check=False