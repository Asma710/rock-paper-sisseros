import random

def play_game():
    options = ['rock', 'paper', 'scissors']

    while True:
        user = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user not in options:
            print("Invalid choice.")
            continue

        computer = random.choice(options)
        print(f"You: {user}, Computer: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user, computer) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]:
            print("You win!")
        else:
            print("You lose!")

        if input("Play again? (yes/no): ").strip().lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    play_game()
