# David Hendershot

def main_menu(): # Mani menu text
    print("Dragon Text Adventure Game")
    print("Collect all 6 items to win the game or be killed by Ghost Ramsley")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'itemname'")

def show_status(currentRoom, inventory, rooms): # Show status
    print('---------------------------')
    print('You are in the', currentRoom)
    print('Inventory :', inventory)
    print('Valid Moves:', validMoves(currentRoom, rooms))
    if 'item' in rooms[currentRoom] and rooms[currentRoom].get('item') not in inventory: # If there is a item in current room and player does not have the item
        print('You see a ', rooms[currentRoom].get('item')) # Print that the player sees the item
    print('---------------------------')
    print('Enter your move:')

def validMoves(currentRoom, rooms):
    directions = {'South', 'West', 'North', 'East'}
    validMoves = []
    for direction in rooms[currentRoom]:
        if direction in directions:
            validMoves.append(direction)
    return validMoves

def main():
    main_menu() # Call main menu function
    rooms = { # Dictionary list to store directions, items and ghosts
        'Kitchen': {'South': 'Living Room', 'West': 'Library', 'North': 'Bedroom', 'East': 'Garage', 'item': 'Knife'},
        'Library': {'East': 'Kitchen', 'item': 'Book'},
        'Bedroom': {'South': 'Kitchen',  'East': 'Bathroom', 'item': 'Clothing'},
        'Bathroom': {'West': 'Bedroom'},
        'Garage': {'West': 'Kitchen', 'North': 'Basement', 'item': 'Keys'},
        'Basement': {'South': 'Garage', 'item': 'Shied'},
        'Living Room': {'North': 'Kitchen', 'East': 'Entrance', 'item': 'Phone'},
        'Entrance': {'West': 'Living Room', 'ghost': 'Ramsley'}
    }

    inventory = [] # Empty list to store users inventory in

    currentRoom = 'Kitchen' # Players start location

    while True: # While game is active
        show_status(currentRoom, inventory, rooms) # Call show status function
        user_input = input('>').split() # Get users input and split it

        if len(user_input) >= 2 and user_input[0].lower() == 'go' and user_input[1].capitalize() in rooms[currentRoom].keys(): # If list has 2 items, the first item is 'go', and the second item is a valid move for current room.
            currentRoom = rooms[currentRoom].get(user_input[1].capitalize()) # Set the players new room
        elif len(user_input) >= 2 and user_input[0].lower() == 'go': # If list has 2 items, the first item is 'go' and the second item is not a valid direction
            print("Invalid move!") # Print that it is a invalid move

        if len(user_input) >= 2 and user_input[0].lower() == 'get' and user_input[1].capitalize() in rooms[currentRoom].get('item'): # If list has 2 items, the first item is 'get' and the current room has a item
            if user_input[1].capitalize() not in inventory: # If the user does not already have that item
                inventory.append(user_input[1].capitalize()) # Add the item to there inventory
            else:
                print('You already have the', user_input[1].capitalize()) # If they already have the item, print that they already have it
        elif len(user_input) >= 2 and user_input[0].lower() == 'get': # If list has 2 items, the first item is 'get' and the second item is not in the room
            print('Unable to get the', user_input[1].capitalize()) # Print that they are unable to get that item.

        if 'ghost' in  rooms[currentRoom].keys() and len(inventory) == 6: # If ghost is in current room and user has 6 inventory items
            print('You won') # Print they won!
            break # Break from loop
        elif 'ghost' in  rooms[currentRoom].keys() and len(inventory) != 6: # If ghost is in current room and user does not have 6 inventory items
            print('You lost') # Print they lost!
            break # Break from loop

        if user_input[0].lower() != 'go' and  user_input[0].lower() != 'get': # If command does not start with go or get
            print('Invalid command!') # Print invalid command!

if __name__ == '__main__':
    main() # Call main function