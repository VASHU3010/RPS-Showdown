import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your Move = Rock, Paper, Scissor :: ")
computer_choice = random.choice(item_list)

print(f"User Choice :: {user_choice}, Computer Choice :: {computer_choice}")

if (user_choice == computer_choice):
    print("Both chooses same, hence MATCH TIE !!!")

elif (user_choice == "Rock"):
    if computer_choice == "Paper":
        print("Paper covers Rock, hence COMPUTER WINS !!!")
    else :
        print("Rock smashes Scissor, hence YOU WIN !!!")

elif (user_choice == "Paper"):
    if computer_choice == "Rock":
        print("Paper covers Rock, hence YOU WIN !!!")
    else :
        print("Scissor cuts Paper, hence YOU WIN !!!")

elif (user_choice == "Scissor"):
    if computer_choice == "Paper":
        print("Scissor cuts Paper, hence YOU WIN  !!!")
    else :
        print("Rock smashes Scissor, hence COMPUTER WINS !!!")

