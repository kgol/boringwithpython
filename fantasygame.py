
def displayInventory(inventory):
    string=''
    for i in inventory.keys():
        string += i+'\n'

    print(inventory)
    print(sum(inventory.values()))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            addedItems.count(addedItems[i])
            value = int(inventory.get(addedItems[i], 0))
            value+=1
            x = {addedItems[i]: value}
            inventory.update(x)
        else:
            y = {addedItems[i]: 1}
            inventory.update(y)
    return inventory

inv ={'gold coin':5, 'dagger': 6}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin','dagger','dagger', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)