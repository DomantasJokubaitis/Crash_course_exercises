def display_inventory(inv):
    total = 0
    for k, v in inv.items():
        print(v, k)
        total += v
    print(f"Total number of items: {total}")

def addToInventory(inventory, loot):
    for item in loot:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1


inv = {"gold coin" : 42, "rope" : 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
addToInventory(inv, dragon_loot)
display_inventory(inv)