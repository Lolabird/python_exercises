# Runestone.Academy thinkcspy course
# Chapter 12
# Problem 2

def add_fruit(inventory, fruit, quantity=0):
    
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity
        
    return inventory

# make these tests work...
new_inventory = {}
print(new_inventory)
add_fruit(new_inventory, 'strawberries', 10)
#  test that 'strawberries' in new_inventory
print(new_inventory.keys())
#  test that new_inventory['strawberries'] is 10
print(new_inventory)
add_fruit(new_inventory, 'strawberries', 25)
#  test that new_inventory['strawberries'] is now 35)
print(new_inventory)