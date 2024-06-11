import random
#VARIBLES/CONSTANTS
EVENTS = [["ma"],["la"]]
ACTIONS = [[["f","e","a"],[0,1,1]],[["s","i"], [0,1]]]
CONSIQUENCES = []
ARMOR_FORMAT = "{}    type: {}   health points: {}"
WEPON_FORMAT = "{}    type: {}   damage: {}   hit chance: {}"
#the numbers in the items list are: first number = damage/health points, second = chance to hit 
equipped_items = [["cannnon","wepon",15,0.5],["basic armor","armor",20]]
inventory_items = [["sword","wepon",5,1],["mediam armor","armor",25],["bow","wepon",7,0.8],["gun","wepon",10,0.9]]
ALL_ITEMS = ["cannon", "basic armor", "sword", "knife", "bow", "gun"]
ENEMYS = [["scout",10,3],["warrior",15,5],["tank",25,4]]
ATTACK_SUCSESS = "attack sucsessful, you did {} damage\nenemy {} is on {} health"
ENEMY_ATTACK = "{} attacks you. it hits.\n your health: {}\n"
damage_taken = 0


#TODO:
#PUT COMBAT IN STORY LOOP WITH SCRIPTED/RANDOM TIMINGS
#ADD CHECKPOINTS
#MAKE A BETTER WAY TO DO STORY PATHS
#AMMO FOR POWERFUL WEPONS?
#BETTER PROMPTS
#PLAY TEST 
#ADD COLOUR FOR TEXT
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
#BALLENCING WEPONS AND ITEMS
#ADD PUZZELS
#ARMOR AND WEPON PASSIVES?
#ADD MAIN CODE
#DO DEVELOPEMENNT SECTIONS
#MAKE SURE TO TAKE SCREENSHOTS


#-----------------------FUNCTIONS--------------------------
def story_loop():
    path = 0
    x=0
    y=0
    while True:
        print("\n",EVENTS[path][x])
        while y < len(ACTIONS[path][0]):
            print(ACTIONS[path][0][y])
            y+=1
        user = input("which do you chose\ni for inventory\n").lower()
        if user == "i":
            inventory()
            y=0
        elif user in ACTIONS[path][0]:
            for i in range(len(ACTIONS[path][0])):
                if user == ACTIONS[path][0][i]:
                    path = ACTIONS[path][1][i]
                    y=0
                    break
        else:
            print("thats not an action")
            y=0

def health(damagetaken):
    health = equipped_items[1][2] - damagetaken
    return health

def combat(enemytype):
    enemy_damage = 0
    damagetaken = damage_taken
    print(ENEMYS[enemytype][0], "attacks")
    while ENEMYS[enemytype][1]-enemy_damage > 0 and health(damagetaken) > 0:
        user = input("Fight\nitems\nflee\n").lower()
        if user == "fight":
            print("you attack enemy with", equipped_items[0][0])
            if random.random()<equipped_items[0][3]:
                enemy_damage += equipped_items[0][2]
                if enemy_damage > ENEMYS[enemytype][1]:
                    enemy_damage = ENEMYS[enemytype][1]
                print(ATTACK_SUCSESS.format(equipped_items[0][2],ENEMYS[enemytype][0],ENEMYS[enemytype][1]-enemy_damage))
            else:
                print("attack missed :(")
        elif user == "items":
            inventory()
        else:
            print("thats nnot an optionn")
        if ENEMYS[enemytype][1]-enemy_damage > 0:
            if random.random()<0.8:
                damagetaken += ENEMYS[enemytype][2]
                print(ENEMY_ATTACK.format(ENEMYS[enemytype][0],health(damagetaken)))
            else:
                print("enemy attacks. it missed")
    print("battle over")
    return damagetaken

#-------------------INVENTORY FUNCTIONS---------------------

def inventory():
    print_inventory()     
    while True:
        user = input("\ntype (thing) to equip somthing    type exit to exit\n").lower()
        if user == "exit":
            return
                
        for i in range(len(inventory_items)):
            if user == inventory_items[i][0]:
                user = input("what action do you want to proform? (equip, cancel)\n").lower()
                if user == "equip":
                    if inventory_items[i][1]==equipped_items[0][1]:
                        equip(0,i)
                        inventory_items.remove(inventory_items[i])
                    elif inventory_items[i][1]==equipped_items[1][1]:
                        equip(1,i)
                        inventory_items.remove(inventory_items[i])
                    print_inventory()
                    break
                elif user == "cancel":
                    break
                else:
                    print("thats not a command")


def equip(index_value,i):
    print("do you want to swap for", equipped_items[index_value][0])
    user = input("yes/no\n").lower()
    if user == "yes" or user == "y":
        inventory_items.append(equipped_items[index_value])
        equipped_items.remove(equipped_items[index_value])
        equipped_items.insert(index_value,inventory_items[i])
    elif user == "no" or user == "n":
        print("ok")
    else:
        print("thats not a command")

def print_inventory():
    print("\nin inventory:")
    for i in range(len(inventory_items)):
        if inventory_items[i][1] == "wepon":
            print(WEPON_FORMAT.format(inventory_items[i][0],inventory_items[i][1],inventory_items[i][2],inventory_items[i][3]))
        elif inventory_items[i][1] == "armor":
            print(ARMOR_FORMAT.format(inventory_items[i][0],inventory_items[i][1],inventory_items[i][2]))
    print("\nequipped:")
    for i in range(len(equipped_items)):
        if equipped_items[i][1] == "wepon":
            print(WEPON_FORMAT.format(equipped_items[i][0],equipped_items[i][1],equipped_items[i][2],equipped_items[i][3]))
        elif equipped_items[i][1] == "armor":
            print(ARMOR_FORMAT.format(equipped_items[i][0],equipped_items[i][1],equipped_items[i][2]))




story_loop()

