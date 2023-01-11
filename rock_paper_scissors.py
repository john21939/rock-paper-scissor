import random
score = 0
computer_score = 0
#dawd
#dsadssssss

while True:
    choices = ["rock", "paper", "scissor"]

    player = None
    result = random.choice(choices)

    while player not in choices:
        player = input("rock, paper, scissor:").lower()


    if player == result:
        print(f"You:{player}")
        print(f"Computer:{result}")
        print("[TIE!]")

    elif player == "rock" and result == "scissor":
        print(f"You:{player}")
        print(f"Computer:{result}")
        print("[You win]")
        score+=1
    elif player == "scissor" and result == "paper":
        print(f"You:{player}")
        print(f"Computer:{result}")
        print("[You win]")
        score+=1

    elif player == "paper" and result == "rock":
        print(f"You:{player}")
        print(f"Computer:{result}")
        print("[You win]")
        score+=1

    else:
        print(f"You:{player}")
        print(f"Computer:{result}")
        print("[You lose]")
        computer_score +=1


    a = input("play again?(yes/no): ").lower()
    if a == "yes":
        continue
    else:
        print(f"SCORE: \nCOMPUTER:{computer_score} wins\nUSER:{score} wins")


        print("BYE!!!")
        quit()
















