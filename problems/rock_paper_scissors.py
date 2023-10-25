import random
import os

game_on = True
print(" Welcome to ROCK PAPER SCISSOR")
user_name = input("Enter your name == ").capitalize()
user_point = 0
comp_point = 0
while game_on:
    print("ROCK == 1")
    print("PAPER == 2")
    print("SCISSOR == 3")
    user_in = int(input("enter your choice = :"))
    comp_in = random.randint(1, 3)
    print(f"{user_name} choice == {user_in} \t\t\t computer choice == {comp_in}")

    if user_in == 1 and comp_in == 3 or user_in == 2 and comp_in == 1 or user_in == 3 and comp_in == 2:
        print(f"{user_name} is winner")
        user_point += 1
        print(f"{user_name}'s point is == {user_point}")
        print(f"comp's point is == {comp_point}")
        regame = input("would you like to play again \n\"Y\" or \"N\" \n").upper()
        if regame == "Y":
            # To clear the terminal:
            os.system('cls')
            continue
        else:
            if user_point == comp_point:
                print("Tie")
            elif user_point > comp_point:
                print(f"{user_name} is a Winner")
            else:
                print("comp is a Winner")
            break
    elif user_in == comp_in:
        print("tie")
        print(f"{user_name}'s point is == {user_point}")
        print(f"comp's point is == {comp_point}")
        regame = input("would you like to play again \n\"Y\" or \"N\" \n").upper()
        if regame == "Y":
            # To clear the terminal:
            os.system('cls')
            continue
        else:
            if user_point == comp_point:
                print("Tie")
            elif user_point > comp_point:
                print(f"{user_name} is a Winner")
            else:
                print("comp is a Winner")
            break


    elif user_in == 3 and comp_in == 1 or user_in == 1 and comp_in == 2 or user_in == 2 and comp_in == 3:
        print("computer is winner")
        comp_point += 1
        print(f"{user_name}'s point is == {user_point}")
        print(f"comp's point is == {comp_point}")
        regame = input("would you like to play again \n\"Y\" or \"N\" \n").upper()
        if regame == "Y":
            # To clear the terminal:
            os.system('cls')
            continue
        else:
            if user_point == comp_point:
                print("Tie")
            elif user_point > comp_point:
                print(f"{user_name} is a Winner")
            else:
                print("comp is a Winner")
            break
