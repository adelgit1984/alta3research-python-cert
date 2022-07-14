#!/user/bin/env python3
import random

# defining how many times a user won in a session
user_wins = 0

# defining how many times the computer won in a session
computer_wins = 0

# creating a list of options for rock/paper/scissors
options = ["rock", "paper", "scissors"]

# defining variable for inputting user name and printing user input
username = input("Hey there, what's your name?")
print("Hello, " + username)

while True:
  user_input = input("Shall we play some Rock/Paper/Scissors? Type in your selection or type Q to quit:").lower()
  if user_input == "q":
    break

  if user_input not in options:
    continue

   # mapping rock/paper/scissor to int
  random_number = random.randint(0, 2)

  computer_pick = options[random_number]
  print("Computer Picked", computer_pick + ".")

  if user_input == "rock" and computer_pick == "scissors":
    print("You won!")
    user_wins += 1
  elif user_input == "paper" and computer_pick == "rock":
    print("You won!")
    user_wins += 1
  elif user_input == "scissors" and computer_pick == "paper":
    print("You won!")
    user_wins += 1
  else:
    print("You lost.")
    computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("See you next time, " + username + ". Thank you for playing my program!")
