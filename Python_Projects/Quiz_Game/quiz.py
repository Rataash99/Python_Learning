questions = [
    ("What does CPU stands for? ", "central processing unit"),
    ("What does GPU stands for? ", "graphics processing unit"),
    ("What does RAM stands for? ", "random access memory"),
    ("What does PSU stands for? ", "power supply unit")
]
choice = input("\nDo you want to play the QUIZ Gmae? \n")
count = 0

if(choice.lower() == "yes"):
    for q in questions:
        answer = input(f"\n{q[0]}\n")
        if(answer.lower() == q[1]):
            print("\nHurray!!! \nCorrect Answer :)\n")
            count += 1
        else:
            print("\nIncorrect Answer :(\n")

print(f"You have got {count} correct answers! (^_^)\n")
