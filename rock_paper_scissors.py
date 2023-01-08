import random
#test


while True:
    choices = ["rock", "paper", "scissor"]
    result = random.choice(choices)


    answer = input("Would you like to play?: (yes/no)")
    if answer.lower() == "yes":
        person_choice = input("rock,paper,scissor?: ").lower()
    else:
        print("BYE!")

        quit()

    if person_choice == result:
        print(f"You:{person_choice}")
        print(f"Computer:{result}")
        print("[TIE!]")

    elif person_choice == "rock" and result == "scissor":
        print(f"You:{person_choice}")
        print(f"Computer:{result}")
        print("[You win]")
    elif person_choice == "scissor" and result == "paper":
        print(f"You:{person_choice}")
        print(f"Computer:{result}")
        print("[You win]")
    elif person_choice == "paper" and result == "rock":
        print(f"You:{person_choice}")
        print(f"Computer:{result}")
        print("[You win]")
    else:
        print(f"You:{person_choice}")
        print(f"Computer:{result}")
        print("[You lose]")
    continue
















