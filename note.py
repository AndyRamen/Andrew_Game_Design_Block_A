#How to identify whether a integer or not.
#Note: Identify UserInput first.


 
    try:
        guess=int(guess)
        check=True
    except ValueError:
        check=False
    if ValueError:
        print("Dude, put an integer. You've just lost a turn.")
        print()