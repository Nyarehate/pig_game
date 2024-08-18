# library 
import random

## Testing random library
#rolled_num = random.randint(1,6)
#print(roll)

def roll_dice():
    min_val = 1
    max_val = 6
    rolled_num = random.randint(min_val,max_val)   
    return rolled_num

# Returns the value from the above function to debug
""" value = roll_dice()
print(value) """

while True:
    players_num = input("How many players are participating (2-4)? [Input number] ")
    if players_num.isdigit():
        players_num = int(players_num) # force conversion from string to integer
        if 2 <= players_num <= 4:
            break # stop the loop
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Input value is not valid. Retry.")

print("The players will be: ", players_num)

# Defines the max score and the players' scores

max_score = 50
## List comprehension: for each player, create a new array. 
player_scores = [0 for _ in range(players_num)]

print(player_scores)

## Roll dice for a player
while max(player_scores) < max_score:

    # Iterate through the number of players
    for player_idx in range(players_num):
        print("Player ", player_idx + 1, "turn has just started!\n")
        print("Your total score is: ", player_scores[player_idx], "\n")
        tmp_score = 0 # record the current score of the player to let him choose whether he wants to keep going or not

        # Iterate through the rolls of the current players playing
        while True:
            should_roll = input("Would you like to roll the dice (yn)? ")
            if should_roll.lower() != "y":
                break

            value = roll_dice()
            if value == 1:
                print("You rolled a 1, you go back to 0!")
                tmp_score = 0
                break
            else:
                tmp_score += value
                print("You rolled a: ", value)
            
            print("Your score is: ", tmp_score)
        
        player_scores[player_idx] += tmp_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of ", max_score)