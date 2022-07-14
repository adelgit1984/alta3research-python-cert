#!/user/bin/env python3
import random

# creating variable for how many times a user won in a session
user_wins = 0

# creating variable for how many times the computer won in a session
computer_wins = 0

# creating a list of options for rock/paper/scissors
options = ["rock", "paper", "scissors"]

# creating variable for inputting user name and printing user input
username = input("Hey there, what's your name?")
print("Hello, " + username)

# creating while loop for user to input rock/paper/scissors, or quit program
while True:
  user_input = input("Shall we play some Rock/Paper/Scissors? Type in your selection or type Q to quit:").lower()
  if user_input == "q":
    break

 # using continue to force user to enter valid option if they input anything other than rock/paper/scissors/ or q
  if user_input not in options:
    continue

 # rock: 0, paper: 1, scissors: 2
  random_number = random.randint(0, 2)
  
 # using random_number as the index to access string in the options variable & printing computer selection
  computer_pick = options[random_number]
  print("Computer Picked", computer_pick + ".")

 # defining, determining, and printing result of user input versus computer input 
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

# when user quits, print result of how many times user won, how many times computer won
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("See you next time, " + username + ". Thank you for playing my program!")
