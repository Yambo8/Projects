#A compact Python implementation of the classic Rock, Paper, Scissors game — written in only 25 lines, featuring simple logic flow and basic error handling for clean and efficient code.
import random
def game(user,cp):
    if user==cp:
        print("\033[93mNo decision! try again or run away\033[0m\n")
    elif (user == 0 and cp == 2) or (user == 1 and cp == 0) or (user == 2 and cp == 1):
        print("\033[92myou win, good for you!\033[0m\n")
    else:
        print("\033[91myou loose to cp :) try again or exit and carry your shame\033[0m\n")
def main():
    tools = ['rock', 'paper', 'scissors']
    while True:
        user_tool = input("\033[4m\033[1;34mWelcome to Rock Paper Scissors!\033[0m \nFor exit press \033[95m q \033[0m \nPlease choose your weapon:").lower()
        if user_tool == 'q':
            print("\n\033[1;34mUntil next time!\033[0m")
            break
        elif user_tool in tools:
            user_weapon = tools.index(user_tool)
            cp_weapon = random.randint(0,2)
            print("\033[95mYour weapon is:\033[0m",user_tool)
            print("\033[95mThe cp weapon is:\033[0m",tools[cp_weapon])
            game(user_weapon, cp_weapon)
        else:
            print("\033[91mInvalid choice. Please try harder!\033[0m")
if __name__ == "__main__":

    main()
