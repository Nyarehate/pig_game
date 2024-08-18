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

while True:
    players_num = input("How many players are participating (2-4)? [Input number] ")
    if players_num.isdigit():
        players_num = int(players_num) # force conversion from string to integer
        if 1 < players_num <= 4:
            break # stop the loop
        else:
            print("Input value is not valid. Retry.")
