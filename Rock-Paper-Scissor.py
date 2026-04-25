import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your Move = Rock, Paper, Scissor :: ")
computer_choice = random.choice(item_list)

print(f"User Choice :: {user_choice}, Computer Choice :: {computer_choice}")