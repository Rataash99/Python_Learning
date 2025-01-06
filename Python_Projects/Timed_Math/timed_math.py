import time
import random

operators = ["+", "*", "-"]
operand1 = 1
operand2 = 20
total_problems = 5

def generate_problem():
    left = random.randint(operand1, operand2)
    right = random.randint(operand1, operand2)
    operator = random.choice(operators)

    exp = f"{left} {operator} {right}"
    answer = eval(exp)

    return exp, answer

wrong = 0

input("Press Enter to START!")
print("---------------------------")

start_time = time.time()


for problem in range(total_problems):
    exp, answer = generate_problem()

    while True:
        guess = input(f"What would be the answer for this {exp} : ")
        if int(guess) == answer :
            break
        wrong += 1

print("---------------------------")

end_time = time.time() - start_time
print(f"You have completed in {end_time.__floor__()} seconds.\nYou have answered {wrong} wrong answers!\n")