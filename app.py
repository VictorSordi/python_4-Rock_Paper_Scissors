import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = input("Chose one: rock, paper or scissors\n")
list = [rock, paper, scissors]
computer = random.choice(list)

if (player == "rock" and computer == rock):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(rock)
    print("Draw")

elif (player == "rock" and computer == paper):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(rock)
    print("Computer Wins")

elif (player == "rock" and computer == scissors):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(rock)
    print("You Win")

elif (player == "paper" and computer == paper):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(paper)
    print("Draw")

elif (player == "paper" and computer == scissors):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(paper)
    print("Computer Wins")

elif (player == "paper" and computer == rock):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(paper)
    print("You Win")


elif (player == "scissors" and computer == paper):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(scissors)
    print("You Win")


elif (player == "scissors" and computer == scissors):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(scissors)
    print("Draw")

elif (player == "scissors" and computer == rock):
    print("computer = " + str(computer))
    print("player = " + str(player))
    print(scissors)
    print("Computer Wins")

else:
    print("Choose a valid alternative: rock, paper, scissors")
