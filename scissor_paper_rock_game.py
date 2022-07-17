import random

user_wins = 0
computer_wins = 0

choices = ["rock" , "paper" , "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or S to stop => ").lower()
    if(user_input == "s"):
        break

    if user_input not in choices: 
        print("Invalid input...Try again!!")
        continue

    random_num = random.randint(0 , 2)
    # rock => 0
    # paper => 1
    # scissor => 2

    computer_choice = choices[random_num]
    print("Computer selected => ", computer_choice)

    if (user_input == "rock" and computer_choice == "scissor"):
        print("You won !!!")
        user_wins += 1
    elif (user_input == "paper" and computer_choice == "rock"):
        print("You won !!!")
        user_wins += 1

    elif (user_input == "scissor" and computer_choice == "paper"):
        print("You won !!!")
        user_wins += 1

    else:
        print("Computer won !!!")
        computer_wins += 1


print("Your score : " , user_wins , "\nComputer score : ", computer_wins)
print("Have a nice day!!!")
        


