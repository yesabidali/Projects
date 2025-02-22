import random

a = ["Stone", "Paper", "Scissors"]

computer = random.choice(a)
you = input("What is your choice (Stone, Paper, Scissors)? ").capitalize()


if computer == you:
    print(f"Both chose {computer}. It's a draw!")
else:
    if computer == "Stone" and you == "Paper":
        print(f"Computer chose {computer}. You win this time!")
    elif computer == "Stone" and you == "Scissors":
        print(f"Computer chose {computer}. Ahhh You lost to the computer hahaha")
    elif computer == "Paper" and you == "Scissors":
        print(f"Computer chose {computer}. You win this time!")
    elif computer == "Scissors" and you == "Paper":
        print(f"Computer chose {computer}. Ahhh You lost to the computer hahaha")
    elif computer == "Paper" and you == "Stone":
        print(f"Computer chose {computer}. Ahhh You lost to the computer hahaha")
    elif computer == "Scissors" and you == "Stone":
        print(f"Computer chose {computer}. You win this time!")
