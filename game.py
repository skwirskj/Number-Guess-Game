# random number game
import random
import computerGuesses

gameModeMess = """Select a gamemode:\n
1.) User guesses a number\n
2.) Computer guesses a number\n
"""

gameMode = int(input(gameModeMess))

if gameMode == 1:
    # input for the choice and a guess indicator for the number of guesses made.
    input1 = 0
    guessCount = 0
    currGuess = 0
    randomNum = 0

    startingMessage = """
    Welcome to the number guessing game! Choose a number for the range:\n
    1.) A number between 0-10\n
    2.) A number between 0-100\n
    3.) A number between 0-1000\n\n
    """

    input1 = int(input(startingMessage))
    correctInput = False

    while not correctInput:
        if input1 == 1:
            randomNum = random.randrange(0, 10, 5)
            correctInput = True
        elif input1 == 2:
            randomNum = random.randrange(0, 100, 5)
            correctInput = True
        elif input1 == 3:
            randomNum = random.randrange(0, 1000, 5)
            correctInput = True
        else:
            print("Incorrect value, select 1, 2, or 3\n")
            input1 = int(input(startingMessage))

    # Guessing process starts now.
    guessCorrect = False
    while guessCount < 3:
        currGuess = int(input("Guess a number:"))
        print("\n")
        guessCount += 1
        if currGuess == randomNum:
            print(f"The random num was {randomNum} and you guessed {currGuess}, which is correct!\n")
            guessCorrect = True
            break
        else:
            print(f"Incorrect guess of {currGuess}. Try again!\n")
            if currGuess < randomNum:
                print(f"Your guess of {currGuess} is less than the number.\n")
            else:
                print(f"Your guess of {currGuess} is greater than the number.\n")

    if not guessCorrect:
        print(f"The random value was {randomNum}. Sorry you did not guess it. Better luck next time!\n")
else:
    userNum = int(input("Select a random number for the computer to guess:"))
    print('\n')
    computerGuesses.computer_func(userNum)



