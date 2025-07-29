import random

# Computer randomly picks stone(1), paper(-1), or scissor(0)
computer = random.choice([-1, 1, 0])

# Mapping of choices
dict = {"stone": 1, "paper": -1, "scissor": 0}
reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

# User input
you = input("Enter your choice (stone/paper/scissor):\n").lower().strip()  # .strip() removes extra spaces

# Validate input
if you not in dict:
    print("Invalid choice")
else:
    youstr = dict[you]  # Convert user's choice to number

    # Print choices
    print(f"Computer chose - {reverseDict[computer]}, you chose - {reverseDict[youstr]}")

    # Game logic
    if computer == youstr:
        print("It's a draw")
    else:
        if computer == -1 and youstr == 1:     # Paper covers stone → you win
            print("You win") # -1 + 1 = 0
        elif computer == -1 and youstr == 0:   # Paper covers scissor → you lose
            print("You lose") # = -1
        elif computer == 1 and youstr == -1:   # Stone vs paper → you lose
            print("You lose") # = 0
        elif computer == 1 and youstr == 0:    # Stone crushes scissor → you win
            print("You win") # = 1
        elif computer == 0 and youstr == -1:   # Scissor cuts paper → you win
            print("You win") # = -1
        elif computer == 0 and youstr == 1:    # Stone crushes scissor → you lose
            print("You lose") # = 1
        else:
            print("Something went wrong!")
