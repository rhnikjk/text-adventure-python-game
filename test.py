import random
EVENTS = [["ma"],["la"]]
ACTIONS = [[["f","e","a"],[0,1,1]],[["s","i"], [0,1]]]
CONSIQUENCES = []
INVENTORY_FORMAT = "{}"
equipped_items = [["cannnon",1,11,0.7],["basic armor",2,20]]
inventory_items = [["sword",1,5,1],["mediam armor",2,25],["bow",1,7,0.8],["gun",1,10,0.9]]
ALL_ITEMS = ["cannon", "basic armor", "sword", "knife", "bow", "gun"]
ENEMYS = [["scout",10,3],["warrior",15,5],["tank",25,4]]
ATTACK_SUCSESS = "attack sucsessful, you did {} damage\nenemy {} is on {} health"

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
            for p in range(len(ACTIONS[path][0])):
                if user == ACTIONS[path][0][p]:
                    path = ACTIONS[path][1][p]
                    y=0
                    break
        else:
            print("thats not an action")
            y=0
# they cann chose to fight or use items. if they fihgt that can select between a couple of differnnt attacks which have differnt chances to hit and differnt amount of damage if they get attacked by an enemy they lose helth
def health():
    health = equipped_items[1][2]

def combat(enemytype):
    enemy_damage = 0
    print(enemytype, "attacks")
    user = input("Fight\nitems\nflee").lower
    if user == "fight":
        print("you attack enemy with", equipped_items[0][0])
        if random()>equipped_items[0][3]:
            enemy_damage += equipped_items[0][2]
            print(ATTACK_SUCSESS.format(equipped_items[0][2],ENEMYS[enemytype][0],ENEMYS[enemytype][1]-enemy_damage))
        else:
            print("attack missed :(")
    elif user == "items":
        print("")

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
                    elif inventory_items[i][1]==equipped_items[1][1]:
                        equip(1,i)
                    else:
                        equipped_items.append(inventory_items[i])
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
        equipped_items.append(inventory_items[i])
    elif user == "no" or user == "n":
        print("ok")
    else:
        print("thats not a command")

def print_inventory():
    print("\nin inventory:")
    for i in range(len(inventory_items)):
        print(INVENTORY_FORMAT.format(inventory_items[i][0]))
    print("\nequipped:")
    for i in range(len(equipped_items)):
        print(equipped_items[i][0])




story_loop()
