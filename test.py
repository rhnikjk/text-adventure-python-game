EVENTS = [["ma"],["la"]]
ACTIONS = [["f","e","a"],["s","i"]]
CONSIQUENCES = []
INVENTORY_FORMAT = "{}"
equipped_items = ["cannnon","basic armor"]
inventory_items = ["sword","knife","bow","gun"]
ALL_ITEMS = ["cannon", "basic armor", "sword", "knife", "bow", "gun"]
ITEM_CLASIFICATION = [1,2,1,1,1,1]



def story_loop():
    path = 0
    x=0
    y=0
    while True:
        num = len(ACTIONS[path])

        print(EVENTS[path][x])
        while y < num:
            print(ACTIONS[path][y])
            y+=1
        user = input("i for innventory\n").lower()
        if user == "i":
            inventory()
            num = len(ACTIONS[path])

            print(EVENTS[path][x])
            while y < num:
                print(ACTIONS[path][y])
                y+=1
        choise = input("\n")
        if choise == "1":
            path = 1

def inventory():
    print("inn invenntory:")
    for i in range(len(inventory_items)):
        print(INVENTORY_FORMAT.format(inventory_items[i]))
    print("\nEquipped:")
    for i in range(len(equipped_items)):
        print(equipped_items[i])       
    while True:
        user = input("type (thing) to equip somthing    type exit to exit\n").lower()
        if user == "exit":
            return
                
        for i in range(len(inventory_items)):
            if user == inventory_items[i]:
                user = input("what action do you want to proform?\n").lower()
                if user == "equip":
                    equipped_items.append(inventory_items[i])
                    inventory_items.remove(inventory_items[i])
                    print("in inventory:")
                    for i in range(len(inventory_items)):
                        print(INVENTORY_FORMAT.format(inventory_items[i]))
                    print("\nequipped:")
                    for i in range(len(equipped_items)):
                        print(equipped_items[i])
                    break
                elif user == "cancel":
                    break
                else:
                    print("thats not a command")

story_loop()
