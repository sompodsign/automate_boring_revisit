dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {}
def addToInventory(inventory, addedItems):
    
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    print(inventory)

addToInventory(inv, dragonLoot)