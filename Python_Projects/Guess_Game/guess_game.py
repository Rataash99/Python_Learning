import random

guess = 1

def generate_random_guess(guess):
    random_guess = random.randint(0, guess)

    if(random_guess == guess):
        return True
    else:
        return False
    
while True:
    user_guess = input("\nHey guess a number : ")
    if(not user_guess.isdigit()):
        print("\nType a number next time!\n")
        continue

    check = generate_random_guess(int(user_guess))
    if(check):
        print("\nyoohoo! you got it correct! <(^_^)\n")
        break

    else:
        print("you got it wrong! :(\n")
        guess += 1

print(f"You go it right in {guess} guesses!\n")
