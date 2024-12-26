import random
user_pick = input("(s for snake, w for water g for gun) \nEnter your input : ")

picks = ["s", "w", "g"]

computer_pick = random.choice(picks);

def check():
    if user_pick == 's':
        if computer_pick == 'g':
            print("You lost, GUN beats SNAKE")
        elif computer_pick == 'w':
            print("You win SNAKE beats WATER")
        else :
            print("Draw")
    
    elif user_pick == 'w':
        if computer_pick == 'g':
            print("You won, WATER beats GUN")
        elif computer_pick == 's':
            print("You lost, SNAKE beats WATER")
        else :
            print("Draw")

    else:
        if computer_pick == 's':
            print("You won, GUN beats SNAKE")
        elif computer_pick == 'w':
            print("You lost WATER beats GUN")
        else :
            print("Draw")

check()


