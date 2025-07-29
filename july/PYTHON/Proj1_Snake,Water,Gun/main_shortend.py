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

if computer == youstr:
    print("It's a draw")
elif (youstr - computer) % 3 == 1:
    print("You win")
else:
    print("You lose")