import random

def game():
    user_score = 0
    computer_score = 0
    print("Welcome to game")
    while True:
        print("\nChoose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice")
            continue
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nFinal Score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break
game()