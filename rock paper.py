from random import choice

computerChoice = choice(['rock', 'paper', 'scissors'])

print("Welcome to Rock, Paper, Scissors!")
print("The computer has chosen its weapon.")
print("Choose yours.")

humanChoice = ""

playAgain = "yes"

while playAgain == "yes":
    humanChoice = input("rock, paper, or scissors? ").lower()
    computerChoice = choice(['rock', 'paper', 'scissors'])
    print("The computer chose " + computerChoice + ".")
    if humanChoice == computerChoice:
        print("It's a tie!")

    elif humanChoice == "rock":
        if computerChoice == "paper":
            print("You lose!")
        else:
            print("You win!")

    elif humanChoice == "paper":
        if computerChoice == "scissors":
            print("You lose!")
        else:
            print("You win!")

    elif humanChoice == "scissors":
        if computerChoice == "rock":
            print("You lose!")
        else:
            print("You win!")

    else:
        print("That's not a valid choice.")
    playAgain = input("Play again? (yes or no) ").lower()

