import random
def Game(user, computer):
    if user == 'Rock' and computer == 'Scissors':
        return "User is the winner"
    elif user == 'Scissors' and computer == 'Rock':
        return "Computer is the winner"
    elif user == 'Scissors' and computer == 'Paper':
        return "User is the winner"
    elif user == 'Paper' and computer == 'Scissors':
        return "Computer is the winner"
    elif user == 'Paper' and computer == 'Rock':
        return "User is the winner"
    elif user == 'Rock' and computer == 'Paper':
        return "Computer is the winner"
    else:
        return "It's a tie!"
def play(choices):
    while True:
        user_choice = input("\nEnter your choice (Rock/Paper/Scissors) or 'quit' to exit: ").capitalize()
        if user_choice == "Quit":
            print("Thanks for playing! 👋")
            break
        if user_choice not in choices:
            print("Invalid choice! Please enter 'Rock', 'Paper', or 'Scissors'.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        result = Game(user_choice, computer_choice)
        print(result)

choices = ['Rock', 'Paper', 'Scissors']
play(choices)
