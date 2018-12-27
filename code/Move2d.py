#Moving Character in 2D Plane
'''
Made by a beginner
'''
arena = [] # This is a map file

def make_board(place): #Generates map terrain
    for i in range(5):
        place.append(["O"] * 5)

def list_to_string(alist): #Makes map easier to read
    for i in alist:
        print(" ".join(i))

make_board(arena) #Calling the function

prev_char_y = 2 # Keeping track of player's last movement
prev_char_x = 2 #Keeping track of player's last movement
char_y = 2 #Keeping track of player's current movements
char_x = 2 #Keeping track of player's current movements
arena[char_x][char_y] = "X" #What is used to show player pos.
list_to_string(arena) #Shows map with player
go = True # Loop :)
while True:
    try:
        while go:
            print("You are: \nX") #Remind player where he or she is (\n means new line)
            control = input("Move left, right, up, down, or stop?") #Ask what player wants to do
            control = control.lower() #Converts player input to lowercase
            if control == "left": #If left
                char_x = char_x - 1
            elif control == "right":# If right
                char_x = char_x + 1
            elif control == "up": #If up
                char_y = char_y - 1
            elif control == "down": #If down
                char_y = char_y + 1
            elif control == "stop": #If player wants to stop
                go = False
            elif control is not "left" or control is not "right" or control is not "down" or control is not "up":
                print("Please enter a proper direction") #If it's not one of those commands
            arena[prev_char_y][prev_char_x] = "O" #Removes previous player position marker
            arena[char_y][char_x] = "X" #Adds current player position marker (Y, X) instead of (X, Y)
            prev_char_y = char_y #Sets the previous y to the current y
            prev_char_x = char_x #Sets the previous x to current x
            list_to_string(arena) #Prints map
    except IndexError:
        print("That's out of range, please pick somewhere else to move")
        char_y = prev_char_y
        char_x = prev_char_x
        arena[char_y][char_x] = "X"
        list_to_string(arena)