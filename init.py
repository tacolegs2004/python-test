import random

def get_choices():
    player_choice = input("rock, paper or scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player} and computer chose {computer}")
    if player == computer:
        return "tie"
    elif player == "rock":
        if computer == "paper":
            return "paper covers rock. you lose"
        if computer == "scissors":
            return "rock smashes scissors! you win!"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        if computer == "scissors":
            return "scissors cuts paper. you lose."
    elif player == "scissors":
        if computer == "rock":
            return "rock smashes scissors. you lose"
        if computer == "paper":
            return "scissors cuts paper! you win!"
    else:
        return "that is not a valid option"
        

choices = get_choices()

result = check_win(choices["player"], choices["computer"])
    
print(result)
