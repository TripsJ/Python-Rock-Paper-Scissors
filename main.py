import random


def get_choices() -> dict | str:
    options = ["rock", "paper", "scissors"]
    player_choice = input(" select Rock, Paper or Scissors: ")
    if player_choice.lower() in options:
        computer_choice = random.choice(options)
        choices = {"computer": computer_choice, "player": player_choice}
        return choices
    else:
        return "Invalid player choice"


def check_win(player_choice: str, computer_choice: str) -> str:
    if player_choice.lower() == computer_choice:
        return "Draw"
    elif player_choice.lower() == "rock":
        if computer_choice == "paper":
            return "Computer wins"
        else:
            return "Player wins"
    elif player_choice.lower() == "paper":
        if computer_choice == "scissors":
            return "Computer wins"
        else:
            return "Player Wins"
    elif player_choice.lower() == "scissors":
        if computer_choice == "paper":
            return "Player Wins"
        else:
            return "Computer Wins"
    else:
        return "invalid input"


choices = get_choices()
if type(choices) == str:
    print(choices)
else:
    print("Computer chose: " + choices.get("computer"))
    print("Player chose: " + choices.get("player"))
    print(check_win(choices.get("player"), choices.get("computer")))
