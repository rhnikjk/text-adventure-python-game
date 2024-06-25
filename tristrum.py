import random
#VARIBLES/CONSTANTS
CONSEQUENCES = []
STORY_EVENTS = [["You crash land on a planet that is covered in forest and does not show many signs of life. you open your eyes and look around, you are on a cliff overlooking a vast expanse of valleys and hills. You check the damages on your spaceship and see that  there is an engine part missing. Looking closer you can make out the silhouettes of buildings, many of which are crumbling and abandoned. You stand up and look around. There are two paths leading down from the cliff. One path looks simple leading through a forest before coming out far below the other path is steep and jagged leading straight down. What path do you choose?",
                 "You start descending down the path towards the forest; the path is wide and slightly overgrown. Small pink bugs fly around you as you start descending into the forest, as you enter the forest everything seems quiet the bugs have gone. Looking around you, you can see large tubular plants among the trees. You reach out to touch one but as you do it suddenly moves in a long sweeping motion you roll out of the way narrowly missing you, as it swings past you can see that the large stem is covered in spikes that seem to be leaking a dark reddish substance which sizzles as it hits the ground.\nyou look off into the distance you see a spire of smoke, you start walking towards it not sure of what you might find. As you near the source of the smoke, you are shocked to see people walking around a crumbling village. You stand up and start walking towards the people. One of them approaches you cautiously holding something. It is a small wooden vial of a purple liquid gesturing to their heart then to the ground. you take the potion. The villager talks about how two years ago an asteroid crashed into the planet wiping out many of the population and with it came the plants. The leader is unknown but you must stop him. We have become far too weak and we are barely able to survive here, let alone travel. You must go. Would you like to accept this quest?",
                 "You decide to accept the quest the villagers cheer. one of them comes forward with a new set of armour. you gratefully take it, thanking the villager you pull off your armour and put on the new one. It is heavy but much better than a broken one. You thank the villagers and start walking in the direction of the boss.",
                 "You walk towards the direction of the boss you soon reach the area but you can't see anything a large mist washes over you and the ground starts to shake as the head of a giant Venus fly trap rises up it stares at you, examining its prey you draw your weapon and brace for the plant to attack the venus fly trap lunges towards you, it narrowly misses you as you roll out of the way and you can hear its mouth close with a loud click."],["You start scaling down the cliff cautiously watching every steep rock crumble below your feet as you descend the cliff, as you continue the cliff starts to shake, you cling to the rocks but you are shaken free you are now sliding down the cliff at an alarming speed. It seems like forever but eventually you crash into the side of one of the structures that you had seen it crumbles giving way as you crash through it before coming to a stop. You are sore and tired but at least you are in one piece, in the corner of the structure you notice a container with a long mediaeval-looking spear you pick it up, examining it. the hilt is made from a green material with a texture similar to wood but much smoother. You decide that it will be helpful and leave the building with the spear in hand. You also find some bread sitting just outside the building\nYou decide to take a rest in the shelter of the abandoned buildings, and think about where to go to find your engine part. You look around and see a fire in the distance, it could be another wreck. Do you go to the engine part or search around the base of the cliff where you crashed?",
                 ],["The villagers cower in fear and let you through, do you leave or kill the rest?"]]
ACTIONS = [[[["forest path",0],["cliff path",1]],[["yes",2],["no",3]]],[[["act3",0],["act4",0],["act5",1]],[["this is path 1",0]]]]
ARMOR_FORMAT = "\033[1m{}    \033[22m\033[3mtype: {}   health points: {}\033[23m"
WEAPON_FORMAT = "\033[1m{}    \033[22m\033[3mtype: {}   damage: {}   hit chance: {}\033[23m"
CONSUMABLE_FORMAT = "\033[1m{}    \033[22m\033[3mtype: {}   heals: {}\033[23m"
cowardice = [0]
#the numbers in the items list are: first number = damage/health points, second = chance to hit 
equipped_items = [["cannon","weapon",15,0.5],["basic armor","armor",20]]
inventory_items = [["food","consumable",10],["sword","weapon",5,1],["medium armor","armor",25],["bow","weapon",7,0.8],["gun","weapon",10,0.9],["stick","weapon",1,1]]
ALL_ITEMS = [["saussage doge", "consumable", 50],["flying squid", "consumable", 35]]
ENEMIES = [["scout",10,3],["warrior",15,5],["tank",25,4]]
ATTACK_SUCSESS = "attack sucsessful, you did {} damage\nenemy {} is on {} health"
ENEMY_ATTACK = "{} attacks you. it hits.\n\033[1m\033[31myour health: {}\n\033[0m"
damage_taken = [0]
checkpoint = [0,0]
PET_OPTIONS = ["Saussage Doge","Flying Squid"]
PETS =[0,1]
CHECKPOINTS = [[2,0],[7,1],[11,0]]
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
            print("8 lister street")
def pet():
    ramdom = random.choice(PETS)
    pet = PET_OPTIONS[ramdom]
    inventory_items.append(ALL_ITEMS[ramdom])
    print("You take",pet,"on your adventure")
    namepet=input("What would you like to name your companion\n")
    print("your pet is now named",namepet,"you love it very much")




def story_loop():
    
    #ask robert bofore modifying any related code
    #path is the story path the event and actions are on
    path = 0
    # x is how far down the path you are
    x=0
    while True:
        createcheckpoint(path, x)
        import textwrap
        text = (STORY_EVENTS[path][x])
        wrapped_text = textwrap.fill(text, width=40)
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



def createcheckpoint(path, x):
    for i in range(len(CHECKPOINTS)):
            if path == CHECKPOINTS[i][0] and x == CHECKPOINTS[i][1]:
                checkpoint.clear()
                checkpoint.insert(0,CHECKPOINTS[i][0])
                checkpoint.insert(1,CHECKPOINTS[i][1])
                CHECKPOINTS.remove(CHECKPOINTS[i][0])
                CHECKPOINTS.remove(CHECKPOINTS[i][1])


                
            
            print("That is not an option")
                
def scripted_event():
    #someone needs to make this
    print(".")

def boss_battle():
    print(".")

def health():
    health = equipped_items[1][2] - damage_taken[0]
    return health

def combat(enemytype):
    enemy_damage = 0
    print(ENEMIES[enemytype][0], "attacks")
    while ENEMIES[enemytype][1]-enemy_damage > 0 and health() > 0:
        user = input("\033[33mFight\nitems(i)\nflee\n\033[0m").lower()
        while True:
            if user == "fight":
                print("you attack enemy with", equipped_items[0][0])
                if random.random()<equipped_items[0][3]:
                    enemy_damage += equipped_items[0][2]
                    if enemy_damage > ENEMIES[enemytype][1]:
                        enemy_damage = ENEMIES[enemytype][1]
                    print(ATTACK_SUCSESS.format(equipped_items[0][2],ENEMIES[enemytype][0],ENEMIES[enemytype][1]-enemy_damage))
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



pet()
inventory()

