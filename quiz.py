def new_game():
    guesses = []
    correct_guesses = 0
    question_no = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_no - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_no += 1
    
    display_score(correct_guesses, guesses)

def check_answer(key, guess):
    if key == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end = " ")
    print()
    print("Guesses: ", end = "")
    for i in guesses:
        print(i, end = " ")

    score = int(correct_guesses / len(questions) * 100)
    print()
    print("Your score is: " + str(score))
    
def play_again():
    play_again = input("Play again? (Y/N): ").lower()
    if play_again != "y":
        return False
    else:
        return True

questions = {
    "Who created Python?: ": "D",
    "What year was Python created?: ": "B",
    "Which comedy group is Python tributed to?: ": "C",
    "Is the Earth flat?: ": "A"
}

options = [
    ["A. Christiano Ronaldo", "B. Lionel Messi", "C. Lady Gaga", "D. Guido van Rossum"],
    ["A. 1990", "B. 1991", "C. 1992", "D. 1993"],
    ["A. Lonely Island", "B. One Direction", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]
]

new_game()
while play_again():
    new_game()

print("Bye!")