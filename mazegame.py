import time

# Make a room class
# Room.description is a string describing the appearance of the room
# Room.damage is a list of the damage done, text describing the damage happening, and the number of times the damage can be triggered.
# if the damage can be triggered infinite times, then Room.damage[3] == 'permanent'
# Room.exits is a dictionary of directions of exits and the rooms they lead to.
# Room.exits must be filled after the rooms are instantiated using Room.add_exit()
class Room:
    def __init__(self, description, damage, exits):
        self.description = description
        self.damage = damage
        self.exits = exits

    def get_location(self):
        return self.location

    def get_description(self):
        return self.description

    def get_damage(self):
        return self.damage

    def get_exits(self):
        return self.exits

    def add_exit(self, direction, room):
        self.exits[direction] = room

class Player:
    def __init__(self, health, currentRoom):
        self.health = health
        self.currentRoom = currentRoom

    def get_health(self):
        return self.health

    def get_currentRoom(self):
        return self.currentRoom

    def get_health_text(self):
        if self.health == 100:
            return "You are the picture of perfect health"
        elif 75 < self.health < 100:
            return "You are walking with a limp, wincing with every step."
        elif 50 < self.health < 75:
            return "Your head is spinning.  You feel weak and tired."
        elif 25 < self.health < 50:
            return "Every muscle in your body burns.  You can barely take another step."
        elif 0 < self.health < 25:
            return "You've never felt so tired.  You are on death's door."

# A function to change the room a player is in
# if checks to see if the second half of the go command is in the player's room's list of keys
# if so, it changes the player's current room to that room, and does any damage
def enter_room(action, a_player):
    if action[3:] in a_player.get_currentRoom().get_exits().keys():
        a_player.currentRoom = a_player.get_currentRoom().get_exits()[action[3:]]
        trigger_damage(a_player)
    else:
        print("You can't go that way.")

# A function that does any damage to the player
# If the room always does damage to the player, it does damage
# If the room temporarily does damage to the player, it does damage and decreases the counter by 1
def trigger_damage(a_player):
    if type(a_player.currentRoom.get_damage()[2]) == str:
        if a_player.currentRoom.get_damage()[0] > 0:
            print(a_player.currentRoom.get_damage()[1])
            a_player.health -= a_player.currentRoom.get_damage()[0]
    elif type(a_player.currentRoom.get_damage()[2]) == int:
        if a_player.currentRoom.get_damage()[2] > 0:
            print(a_player.currentRoom.get_damage()[1])
            a_player.health -= a_player.currentRoom.get_damage()[0]
            a_player.currentRoom.get_damage()[2] -= 1

# 5 rooms arranged in a cross
entrance = Room('You are in an the beginning of a maze.  The thick stone walls loom ominously over you, too tall to climb.  \nThe path continues to the north.', [0, '', 'permanent'], {})
roomOne = Room('You are in an empty passageway which leads north and south.', [0, '', 'permanent'], {})
roomTwo = Room('You are in an empty passageway.  From here you can go north, east, and south. \nThere is a noise coming from the east.', [0, '', 'permanent'], {})
roomThree = Room('You find yourself in an L shaped passageway room which leads west and south.', [30, 'As you turn the corner, you hear a horrible sound.  \nYou fall to the ground before you can realize what is happening.  \nThere is a cold inky blackness clinging to your left leg.  \nYou manage to kick it off with your shoe, but cold remains, deep in your bones.', 1], {})
roomFour = Room('You come upon a dead end, the only way out is to the north.  \nOne of the walls here is stained a dark red, and has scratches gouged into it.', [0, '', 'permanent'], {})
roomFive = Room('This hallway leads north and south.  You can hear what sounds like whispering in the distance.', [0, '', 'permanent'], {})
roomSix = Room('You come upon a corner, leading south and west.  \nTo the south you think you can almost hear voices.', [0, '', 'permanent'], {})
roomSeven = Room('This path of the maze leads from east to west. \nIt seems to stretch on for miles behind you, though you know that cannot possible be true.', [0, '', 'permanent'], {})
roomEight = Room('The maze forms a Y here with forks leading north and south, and the third path heading west. \nOn the wall between the north and south forks, written in blood is the word "Choose". \nTo the south you can feel a cold breeze.', [0, '', 'permanent'], {})
roomNine = Room('As you follow the path, it dead ends. In the corner in front of you is a skeleton.', [90, 'One of the shadows oozes towards you.  The gibbering terror surrounds you before you can escape. \nIt spreads up your body, smothering you.  \nYou pull and claw at it, just barely managing to get free as it slithers back into the shadows.', 1], {})
roomTen = Room('The passage deadends here, as unremarkable as any of the others.', [0, '', 'permanent'], {})

# Add exits to each room
entrance.add_exit('north', roomOne)
roomOne.add_exit('north', roomTwo)
roomOne.add_exit('south', entrance)
roomTwo.add_exit('north', roomFive)
roomTwo.add_exit('east', roomThree)
roomTwo.add_exit('south', roomOne)
roomThree.add_exit('south', roomFour)
roomThree.add_exit('west', roomTwo)
roomFour.add_exit('north', roomThree)
roomFive.add_exit('north', roomSix)
roomFive.add_exit('south', roomTwo)
roomSix.add_exit('south', roomFive)
roomSix.add_exit('west', roomSeven)
roomSeven.add_exit('east', roomSix)
roomSeven.add_exit('west', roomEight)
roomEight.add_exit('north', roomTen)
roomEight.add_exit('east', roomSeven)
roomEight.add_exit('south', roomNine)
roomNine.add_exit('north', roomEight)
roomTen.add_exit('south', roomEight)

# Make a player with 100 health in the entrance
player = Player(100, entrance)

# Start the player in the central room, and begin the game
currentRoom = entrance
playing = True
while playing:
    print()
    print()
    print(player.get_currentRoom().get_description())
    action = input('What do you want to do? ')
    if action[:2] == 'go':
        enter_room(action, player)
    elif action == 'health':
        print(player.get_health_text())
    elif action == 'quit':
        playing = False
    else:
        print("I don't understand.")
    if player.get_health() <= 0:
        print('You have died')
        playing = False
    if player.get_currentRoom() == roomTen:
        print('The passage deadends here.')
        print('You prepare to return the way you came.  But you give the passage one last look.')
        time.sleep(2)
        print('There is a door that was not there before on the north wall.')
        time.sleep(2)
        print('Your arm reaches out to open the door.')
        time.sleep(3)
        print('As the door cracks, a blinding light washes over you.')
        time.sleep(1)
        print('GAME OVER')
        playing = False
