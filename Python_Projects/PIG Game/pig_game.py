import random;
def roll():
    min_dice_num = 1
    max_dice_num = 6
    dice_num = random.randint(min_dice_num, max_dice_num)

    return dice_num

while True:
    players = input("Enter number of Players (2-4) : ")

    if players.isdigit() :
        players = int(players)
        if 1 < players <= 4:
            break
        else:
            print("Must be between 2-4")

    else :
        print("Invalid!, Try again!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\n player number {player_idx + 1} turn has just started")
        print(f"Your Total score is {player_scores[player_idx]}\n")

        current_score = 0

        while True:
            would_roll = input("Would you like to roll (y) : ")

            if would_roll.lower() != 'y':
                break

            else :
                value = roll()
                if value == 1:
                    current_score = 0
                    print("you rolled a 1, Your Turn is over!")
                    break

                else :
                    print(f"You rolled {value}!")
                    current_score += value

                print(f"Your score is {current_score}!")

        player_scores[player_idx] += current_score
        print(f"You scored {player_scores[player_idx]}")

max_score = max(player_scores)
winner = player_scores.index(max_score)
print(f"Player number {winner + 1} is the winner with a score {max_score}")





