#Define rooms and a basic map
rooms = {
    "main hall":{
        "description": "You are now in the main hall of the castle.",
        "west": "dungeon",
        "items": ["torch", "knife", "gun", "golden key"]
    },
    "dungeon":{
        "description": "You are in now the dungeon where keys to other rooms or treasures could be found! Remember, you're not alone though!",
        "east": "main hall",
        "items": ["souvenir","skeleton", "treasure chest"]
    }
}
#Global variables
current_room = "main hall" 
room_1 = "dungeon"
#Player inventory
inventory = []     #Empty list so that when the player collects items, those will be added to the list

#Print a welcome msg and room desc
def welcome_msg():
    print("\nWelcome to the Haunted Castle! Rest assured this is going to be a fun and spooky adventure!")
    #print(rooms[current_room]["description"])
    print("These commands below will come in handy during your time here.")

#Get users to input a command from the list and return them as lower case 
def get_command():
    #Ensure to add additional inventory commands that start with "take" to factor into the game logic
    command_options = ["look", "go west","go east", "take torch", "take knife", "take gun", "take golden key", 
                       "take souvenir", "take skeleton", "take treasure chest", "inventory", "help", "quit"]
    print("\nYour command options are: ")
    for option in command_options:
        print(f"{option}")
    return input("\nPlease enter a command from this list to continue: ").lower()

#Execute actions for commands entered by users
def execute_command(command):
    global current_room

    #Quits the game
    if command == "quit":
        print("You have chosen to quit the game. Thank you for playing!")
        return False
    #Check current room and print room items
    elif command == "look":
        print(rooms[current_room]["description"])
        if rooms[current_room]["items"]:
            print("\nItems in this room are:")
            for i in rooms[current_room]["items"]:
                print(i)
    #Check for current room direction and update to new room 
    elif command.startswith("go "):
        direction = command.split()[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print(rooms[current_room]["description"])
        else:
            print("You can't go that way!")
    #Based on the input command, check current room items, remove items from room and add to player inventory
    elif command.startswith("take "):
        item = command.split(" ", 1)[1]
        if item in rooms[current_room]["items"]:
            rooms[current_room]["items"].remove(item)
            inventory.append(item)
            print(f"You have now collected the {item}!")
        else:
            print(f"There is no {item} here!")
    #Check player inventory and print
    elif command == "inventory":
        if inventory:
            print("You are carrying the following inventory: ")
            for j in inventory:
                print(j)
        else:
            print("You are not carrying anything!")
    elif command == "help":
        print("Here are the in game commands: look, go [direction], take [item], inventory, quit")
    else:
        print("Command not recognized! Please type 'help' for a list of commands.")
    
    return True

def main():
    welcome_msg()
    while True:
        cmd = get_command()
        if not execute_command(cmd):
            break
                
if __name__ == "__main__":
    main()