import random
import time


def computer_func(userNum):
    welcomeMessage = f"Welcome to the computer guesser! The computer will try and guess your value of {userNum}"
    menuMessage = """
    Choose a number for the range:\n
    1.) A number between 0-10\n
    2.) A number between 0-100\n
    3.) A number between 0-1000\n\n
    """

    computerGuess = 0

    print(welcomeMessage)
    print('\n')
    userInput = int(input(menuMessage))
    upperRange = 0
    inputCorrect = False

    while not inputCorrect:
        if userInput == 1:
            upperRange = 10
            inputCorrect = True
        elif userInput == 2:
            upperRange = 100
            inputCorrect = True
        elif userInput == 3:
            upperRange = 1000
            inputCorrect = True
        else:
            print("Incorrect value for menu! Pick a number 1-3.\n")
            userInput = int(input(menuMessage))

    guessNum = 0
    while guessNum < 3:
        computerGuess = random.randrange(0, upperRange, 5)
        guessNum += 1
        if computerGuess == userNum:
            print(f"The computer correctly guessed your number, {userNum}, in {guessNum} guesses.\n")
            break
        else:
            print(f"The computer's {guessNum} guess of {computerGuess} is incorrect!\n")
        time.sleep(3)