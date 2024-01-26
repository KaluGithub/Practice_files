# Fruit Inventory with Dictionary Practice
# Carrot.whiteman.edu
# Q1.  Function definition
# By Mona




def add_fruit(inventory, fruit, quantity =0):
     inventory = {}
     if fruit in inventory:
         inventory[fruit] += quantity
     else:
        inventory[fruit] = quantity
     return inventory

def main():
    print(add_fruit("inventory","strawberries", 10))
    # print("strawberries" in inventory)
    # print(new_inventory["strawberries"] == 10)
    # print(add_fruit("strawberries", 25))
    # print(new_inventory["strawberries"] == 35)

main()