import random
# Define greetings
def greetings():
  greet = print("Hi")
  welcome_message = print("------Welcome to Rock Paper Scissors Game ------------")

# Define get choices function
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  # win if player is computer
  if player == computer:
    return "Its a Tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors!You Win"
    else:
      return "Paper covers rock!You lose"
  elif player == "paper":
    if computer == "rock":
      return "paper covers rock!You Win"
    else:
      return "Rock smashes paper!You lose"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper!You Win"
    else:
      return "Rock smashes scissors!You Lose"


choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)
        
    