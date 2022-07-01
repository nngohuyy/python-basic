import random

def print_choices(computer, player):
    print("Computer: " + computer)
    print("Player: " + player)

def print_win(computer, player):
    print_choices(computer, player)
    print("You win!")

def print_lose(computer, player):
    print_choices(computer, player)
    print("You lose!")

def print_tie(computer, player):
    print_choices(computer, player)
    print("Tie!")

def comparison(computer, player):
    if player == computer:
        print_tie(computer, player)
    elif player == "rock":
        if computer == "paper":
            print_lose(computer, player)
        if computer == "scissors":
            print_win(computer, player)
    elif player == "paper":
        if computer == "scissors":
            print_lose(computer, player)
        if computer == "rock":
            print_win(computer, player)
    else:
        if computer == "rock":
            print_lose(computer, player)
        if computer == "paper":
            print_win(computer, player)

def main():
    while True:
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("Rock, paper or scissors?: ").lower()

        comparison(computer, player)

        play_again = input("Play again? (Y/N): ").lower()
        if play_again != "y":
            break

    print("Bye!")

main()