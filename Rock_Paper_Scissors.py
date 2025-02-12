#start the game
#ask the player to make the move(r,p,s)
#PC would select a move randomly
#PC==player => Tie
#(Palyer == p and PC== Rock)(Player ==R and PC == Scissores) (Player == Scissores and PC == Paper)
#User won / You won
#Any other case
#PC won/  You lose
import random

# Prompt user for input and convert it to lowercase to handle any case input
User = input("What is your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors: ").lower()

# Ensure the input is valid
if User not in ['r', 'p', 's']:
    print("Invalid input! Please choose 'r', 'p', or 's'.")
else:
    pc = random.choice(['r', 'p', 's'])

    print("User's choice: " + User)
    print("PC's choice: " + pc)

    if User == pc:
        print("It's a tie!")
    elif (User == 'p' and pc == 'r') or (User == 'r' and pc == 's') or (User == 's' and pc == 'p'):
        print("You win!")
    else:
        print("You lose!")
