import random

choices = ["rock","paper", "scissor"]
def AI_choice():
    result = random.choice(choices)
    print(result)

answer = input("Would you like to play a game?: (yes/no)")
if answer.lower() == "yes":
    game = input("rock,paper,scissor?: ")
else:
    print("Bye")
    quit()


