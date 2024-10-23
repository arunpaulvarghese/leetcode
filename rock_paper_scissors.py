# Program for stone, paper, scissors

import random

def initialDeclaratin(user,computer):
    if (user == "stone" and computer == "scissors" or
        user == "paper" and computer == "rock" or
        user == "scissors" and computer == "paper"):
        return True
    return False

def get_input():
    user = input("choose stone, paper or scissors")
    user.lower()
    return user

def main():
    user_score = 0
    computer_score = 0
    user = ''
    print("Quit anytime by typing end")
    while (user != "end"):
        print(f'score: {user_score} - {computer_score}')
        computer = random.choice(['stone', 'paper', 'scissors'])
        user = get_input()

        if user == 'end':
            print("goodbye")
        elif user == computer:
            print("both selected the same input")
        # elif user != "stone" or "paper" or "scissors":
        #     print("invalid input")
        elif initialDeclaratin(user, computer):
            print(f"i choose {computer} you win")
            user_score += 1
        else:
            print(f"i choose {computer} you loose")
            computer_score += 1

if __name__ == "__main__":
    main()














