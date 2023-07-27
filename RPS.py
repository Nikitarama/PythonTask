#Random Lib imported
import random 

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice, "computer" : computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} , computer chose {computer} ")
  if player == computer:
    return "Its a tie!";
  elif player == "rock" and computer == "scissors":
    return "Rock smashes scissors! You win"
  elif player == "scissors" and computer == "rock":
    return "Rock smashes scissors! You lose" 
  elif player == "paper" and computer == "scissors":
    return "Scissors cuts paper! You lose!"
  elif computer == "paper" and player == "rock":
    return "Paper eats rock! You lose!"
  elif computer == "rock" and player == "paper":
    return "Paper eats rock! You win!"
  elif computer == "paper" and player == "scissors":
    return "Scissors cuts paper! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)