# Week 02 Lab - Rock, Paper, Scissors Game
# Objective: Use arrays (lists), user input, int conversion, if-statement error handling,
# array indexing, conditionals, and string comparison.

# 1) Define the choices array
choices = ["Rock", "Paper", "Scissors"]

# 2) Get player input (number: 1=Rock, 2=Paper, 3=Scissors)
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

# 3-4) Convert to int + error handling with simple if statements (no try/except needed)
if not playerChoice.isdigit():
    print("Error: Choice must be between 1 and 3.")
    raise SystemExit

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
    raise SystemExit

# 5) Get computer's choice (simulated input for now)
computerChoice = input("Enter computer's choice (1-3): ")

# Convert + validate
if not computerChoice.isdigit():
    print("Error: Choice must be between 1 and 3.")
    raise SystemExit

computerChoice = int(computerChoice)

if computerChoice < 1 or computerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
    raise SystemExit

# 6) Array indexing (lists are 0-indexed, so subtract 1)
playerChoiceName = choices[playerChoice - 1]
computerChoiceName = choices[computerChoice - 1]

print("You chose:", playerChoiceName)
print("Computer chose:", computerChoiceName)

# 7) Determine the winner
if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == 1 and computerChoice == 3:
    print("Rock beats Scissors - You win!")
elif playerChoice == 2 and computerChoice == 1:
    print("Paper beats Rock - You win!")
elif playerChoice == 3 and computerChoice == 2:
    print("Scissors beats Paper - You win!")
else:
    print("You lose!")

# 8) String comparison
if playerChoiceName != "Rock":
    print("You didn't pick the classic Rock...")
