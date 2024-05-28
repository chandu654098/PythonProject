import random

# Define the board size
board_size = 100

# Define the snakes and ladders
snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}

# Define the player starting position
player_position = 0

print("Welcome to Snake and Ladder game!")
print("You are at position 0. Roll the dice to start playing.")

while True:
    # Ask for user input to roll the dice
    input("Press Enter to roll the dice...")
    
    # Roll the dice
    dice = random.randint(1, 6)
    print("You rolled a", dice)
    
    # Move the player
    new_position = player_position + dice
    
    # Check for snakes and ladders
    if new_position in snakes:
        print("Oh no! You landed on a snake at position", new_position)
        player_position = snakes[new_position]
        print("You have been moved to position", player_position)
    elif new_position in ladders:
        print("Yay! You landed on a ladder at position", new_position)
        player_position = ladders[new_position]
        print("You have been moved to position", player_position)
    else:
        player_position = new_position
        print("You are now at position", player_position)
    
    # Check for win
    if player_position >= board_size:
        print("Congratulations, you won!")
        break