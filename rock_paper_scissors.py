import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    quit = False
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock-Paper-Scissors!")
    while(quit == False):
        user_input = input("Enter rock, paper or scissors: ")
        if choices.__contains__(user_input):
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            if user_input == choices[0] and computer_choice == choices[2]:
                print("You win!")
            elif user_input == choices[2] and computer_choice == choices[1]:
                print("You win!")
            elif user_input == choices[1] and computer_choice == choices[0]:
                print("You win!")
            elif user_input == computer_choice:
                print("A tie!")
            else:
                print("You lose!")
        elif user_input == "quit":
            return
        else:
            print("Enter valid choice")

# Run the game
rock_paper_scissors_game()
