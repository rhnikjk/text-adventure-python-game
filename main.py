import random
#VARIBLES/CONSTANTS
CONSEQUENCES = []
STORY_EVENTS = [["mark whips it out","sigma","as","flip"],["racist","as","fella"]]
ACTIONS = [[[["act1",0],["act2",1]],[["this is path0",1]]],[[["act3",0],["act4",0],["act5",1]],[["this is path 1",0]]]]
ARMOR_FORMAT = "\033[1m{}    \033[22m\033[3mtype: {}   health points: {}\033[23m"
WEAPON_FORMAT = "\033[1m{}    \033[22m\033[3mtype: {}   damage: {}   hit chance: {}\033[23m"
CONSUMABLE_FORMAT = "\033[1m{}    \033[22m\033[3mtype: {}   heals: {}\033[23m"
cowardice = [0]
#the numbers in the items list are: first number = damage/health points, second = chance to hit 
equipped_items = [["cannon","weapon",15,0.5],["basic armor","armor",20]]
inventory_items = [["food","consumable",10],["sword","weapon",5,1],["medium armor","armor",25],["bow","weapon",7,0.8],["gun","weapon",10,0.9],["stick","weapon",1,1]]
ALL_ITEMS = ["cannon", "basic armor", "sword", "knife", "bow", "gun"]
ENEMIES = [["scout",10,3],["warrior",15,5],["tank",25,4]]
ATTACK_SUCCESS = "attack successful, you did {} damage\nenemy {} is on {} health"
ENEMY_ATTACK = "{} attacks you. it hits.\n\033[1m\033[31myour health: {}\n\033[0m"
damage_taken = [0]


#TODO:
#PUT COMBAT IN STORY LOOP WITH SCRIPTED/RANDOM TIMINGS
#ADD CHECKPOINTS
#AMMO FOR POWERFUL weaponS?
#BETTER PROMPTS
#PLAY TEST 
#ADD PICKING UP ITEMS
#ADD CONSUMABLES
#ADD STORY
#ADD MORE ENEMY TYPES
#FIX SPELLING MISTAKES
#ADD CHECKPOINTS AND SCRIPTED EVENTS
#ADD BOSS FIGHT
#ADD COMMENTS
#ADD FLEE TO FIGHTS +COWARD ENDING
#ADD DIFFERNNT INPUTS AND MESSAGES IF INPUT IS INVALID
#BALLENCING weaponS AND ITEMS
#ADD PUZZELS
#ARMOR AND weapon PASSIVES?
#ADD MAIN CODE
#DO DEVELOPEMENNT SECTIONS
#MAKE SURE TO TAKE SCREENSHOTS
#todo list (charlie is doing it)


#-----------------------FUNCTIONS--------------------------
def intro():
    input("whats your name" )
    print("I noticed you made a spelling mistake but fair not I can see you were writing Robat :D")
    ready = input( "welcome Robat to ---- Are you ready to play? yes or no\n")
    while True:
        if ready == ("yes"):
            print ("lets jump into it")
            break
        else:
            print("your not funny for typing this")

def story_loop():
    
    #ask robert bofore modifying any related code
    #path is the story path the event and actions are on
    path = 0
    # x is how far down the path you are
    x=0
    while True:
        print(STORY_EVENTS[path][x])
        #prints out available actions for path
        for i in range(len(ACTIONS[path][x])):
            # i counts up all the actions, and the 0 is so it prints only the text
            print("\033[33m",ACTIONS[path][x][i][0],"\033[0m")
        user = input("\033[22mwhich do you chose?\n\033[33mi\033[0m for inventory\n").lower()
        for i in range(len(ACTIONS[path][x])):
            if user == ACTIONS[path][x][i][0]:
                path = ACTIONS[path][x][i][1]
                # if the value of the action you do matches the path you are taking, it moves you forward with the path and if it doesn't match then it resets to 0 as you are taking a new path
                if ACTIONS[path][x][i][1] == path:
                    x+=1
                else:
                    x=0
                break
            # if the user types "i" then it stops and opens the inventory
            elif user == "i":
                inventory()
                break
            else:
                print("that is not an option")
            #if it helps you can think of it like a coordinate system with the 'path's being on one axis and the 'x' on the other.
                
            

def health():
    health = equipped_items[1][2] - damage_taken[0]
    return health

def combat(enemytype):
    enemy_damage = 0
    print(ENEMIES[enemytype][0], "attacks")
    while ENEMIES[enemytype][1]-enemy_damage > 0 and health(damage_taken[0]) > 0:
        user = input("\033[33mFight\nitems(i)\nflee\n\033[0m").lower()
        while True:
            if user == "fight":
                print("you attack enemy with", equipped_items[0][0])
                if random.random()<equipped_items[0][3]:
                    enemy_damage += equipped_items[0][2]
                    if enemy_damage > ENEMIES[enemytype][1]:
                        enemy_damage = ENEMIES[enemytype][1]
                    print(ATTACK_SUCCESS.format(equipped_items[0][2],ENEMIES[enemytype][0],ENEMIES[enemytype][1]-enemy_damage))
                else:
                    print("attack missed :(")
                break
            elif user == "items" or user == "item" or user ==  "i":
                inventory()
                break
            elif user == "flee":
                print("you flee, like a coward. you will regret this later")
                cowardice[0] += 1
            else:
                print("thats not an option")
        if ENEMIES[enemytype][1]-enemy_damage > 0:
            if random.random()<0.8:
                damage_taken[0] += ENEMIES[enemytype][2]
                print(ENEMY_ATTACK.format(ENEMIES[enemytype][0],health()))
            else:
                print("enemy attacks. it missed")
    print("battle over")
    return damage_taken[0]

#-------------------INVENTORY FUNCTIONS---------------------

def inventory():
    print_inventory()     
    while True:
        user = input("\ntype (\033[1mthing\033[0m) to equip somthing    type \033[33mexit\033[0m to exit\n").lower()
        if user == "exit":
            return
                
        for i in range(len(inventory_items)):
            if user == inventory_items[i][0]:
                user = input("what action do you want to proform? (\033[33muse, cancel\033[0m)\n").lower()
                if user == "use":
                    if inventory_items[i][1]==equipped_items[0][1]:
                        equip(0,i)
                        inventory_items.remove(inventory_items[i])
                    elif inventory_items[i][1]==equipped_items[1][1]:
                        equip(1,i)
                    else:
                        damage_taken[0] -= inventory_items[i][2]
                        inventory_items.remove(inventory_items[i])
                        if damage_taken[0] < 0:
                            damage_taken[0] = 0
                    print_inventory()
                    break
                elif user == "cancel":
                    break
                else:
                    print("thats not a command")


def equip(index_value,i):
    print("do you want to swap for", equipped_items[index_value][0])
    user = input("\033[33myes/no\033[0m\n").lower()
    if user == "yes" or user == "y":
        inventory_items.append(equipped_items[index_value])
        equipped_items.remove(equipped_items[index_value])
        equipped_items.insert(index_value,inventory_items[i])
    elif user == "no" or user == "n":
        print("ok")
    else:
        print("thats not a command")

def print_inventory():
    print("\n\033[4min inventory:\033[24m")
    for i in range(len(inventory_items)):
        if inventory_items[i][1] == "weapon":
            print(WEAPON_FORMAT.format(inventory_items[i][0],inventory_items[i][1],inventory_items[i][2],inventory_items[i][3]))
        elif inventory_items[i][1] == "armor":
            print(ARMOR_FORMAT.format(inventory_items[i][0],inventory_items[i][1],inventory_items[i][2]))
        elif inventory_items[i][1] == "consumable":
            print(CONSUMABLE_FORMAT.format(inventory_items[i][0],inventory_items[i][1],inventory_items[i][2]))
    print("\n\033[4mequipped:\033[24m")
    for i in range(len(equipped_items)):
        if equipped_items[i][1] == "weapon":
            print(WEAPON_FORMAT.format(equipped_items[i][0],equipped_items[i][1],equipped_items[i][2],equipped_items[i][3]))
        elif equipped_items[i][1] == "armor":
            print(ARMOR_FORMAT.format(equipped_items[i][0],equipped_items[i][1],equipped_items[i][2]))



story_loop()

