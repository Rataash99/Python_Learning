
master_passw = input("Enter your master password : ")


def add():
    name = input("Enter Account Name : ")
    pwd = input("Enter Password : ")

    with open('defCon_gitKraken.txt', 'a') as f:
        f.write(f"name - {name}, password - {pwd}\n")

def view():
    with open("defCon_gitKraken.txt", 'r') as f:
        for lines in f.readlines():
            print(lines.rstrip())

while True:
    mode = input("Enter '1' to add a new password or '2' to view existing ones or 'q' to quit : ")
    if mode == 'q':
        break
    if mode == '1':
        add()
    elif mode == '2':
        view()
    else:
        print("Please select a Valid Mode!")

