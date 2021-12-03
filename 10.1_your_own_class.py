# Francesca Lozada
# Assignment 10.1
# Creating a class based on a real-world object.

# ACKNOWLEDGEMENTS
# [1] https://www.programiz.com/python-programming/methods/list/index
# Just reminder on how to use index

# [2] https://pynative.com/python-class-variables/#h-modify-class-variables


# Set up the class Item
class Item:
    # Class variable magic_level, which is set as default to 0
    magic_level = 0

    # __init__ function that takes in itself alongside
    # weight, size, and name as arguments
    def __init__(self, weight: int, size: int, name: str):
        self.__weight = weight
        self.__size = size
        self.__name = name
    
    # Get-set functions for each of the private data
    # attributes
    def get_weight(self) -> int:
        return self.__weight
    
    def get_size(self) -> int:
        return self.__size
    
    def get_name(self) -> str:
        return self.__name
    
    # The enchant function, which increases the magic_level
    # class variable by a specified increase_magic integer
    def enchant(self, increase_magic: int) -> int:
        Item.magic_level += increase_magic # [2]
    
    # The curse function, which decreases the magic_level 
    # class variable by a specified decrease_magic integer
    def curse(self, decrease_magic: int) -> int:
        Item.magic_level -= decrease_magic


# Set up the class Weapon, which is derived from 
# Item
class Weapon(Item):
    # Weapon takes in an extra argument damage, which is an 
    # integer value
    def __init__(self, weight: int, size: int, name: str, damage: int):
        # super for referencing the parent class
        super(Weapon, self).__init__(weight, size, name)
        self.__damage = damage
    
    # Get-set function which returns the damage value
    def get_damage(self):
        return self.__damage


# Set up the class Potion, which is derived from
# Item
class Potion(Item):
    # Potion takes in an extra argument healing, which 
    # is an integer value
    def __init__(self, weight: int, size: int, name: str, healing: int):
        # super for referencing the parent class
        super(Potion, self).__init__(weight, size, name)
        self.__healing = healing
    
    # Get-set function which returns the damage value
    def get_healing(self):
        return self.__healing 


# Set up the class Bag
class Bag: 
    # __init__ function that takes in itself alongside
    # size_limit and name as arguments
    def __init__(self, size_limit: int, weight_limit: int):
        # Each of the parameters are instantiated in the __init__,
        # alongside an empty list under self.__items that is used
        # to simulate the 'Bag'
        self.__items = []
        self.__size_limit = size_limit
        self.__weight_limit = weight_limit
        self.__current_size = 0
        self.__current_weight = 0

    # The add function, which takes in itself and an additional
    # argument that is an Item
    def add(self, item: Item):
        # If the limit of the size and weight is not exceeded, the list is appended
        # and the current size and weight are increased by the set size and weight
        # of the items
        if (item.get_size() + self.__current_size <= self.__size_limit) and (item.get_weight() + self.__current_weight <= self.__weight_limit):
            self.__items.append(item)
            self.__current_size += item.get_size()
            self.__current_weight += item.get_weight()
        else:
            # Otherwise, an error message is printed
            print(f"'{item.get_name()}' does not fit in your bag!")
    
    # The inventory function, which returns the names of the items
    # in the bag as a list
    def inventory(self):
        result = []
        for i in self.__items:
            result.append(i.get_name())
        return result

    # Magic method __str__
    def __str__(self) -> str:
        # Set up an empty string
        result = ""
        # Initialize for loop
        for i in self.__items:
            # If the type is a Weapon, concatenate a specific string to the result
            if isinstance(i, Weapon):
                result += f"'{i.get_name()}' - Weapon Damage: {i.get_damage()}\n"
            # If the type is a Potion, concatenate a specific string to the result
            elif isinstance(i, Potion):
                result += f"'{i.get_name()}' - Potion Healing: {i.get_healing()}\n"
            # If the type is an Item, concatenate the name of the item
            elif isinstance(i, Item):
                result += f"'{i.get_name()}'"

        # Replace the last '\n' in the loop with an empty space
        result = result[0:len(result) - 1]
        result += ""

        # Return result
        return result


# DEMO PROGRAM
def main():
    # Creates a bag with a weight and size limit of 10 and 10
    bag = Bag(10, 10)

    # Adds several different potions and weapons to the bag
    bag.add(Potion(1, 1, "Health-1", 1))
    bag.add(Potion(1, 1, "Health-2", 2))
    bag.add(Weapon(5, 2, "Sword-3", 3))
    bag.add(Weapon(5, 3, "Sword-3+", 3))

    # Prints out what just a bag would be
    print(bag)
    
    # Prints out the inventory of the bag using the .inventory() function
    print(bag.inventory())

    # Creates new weapons and potions
    lightning_sword = Weapon(3, 2, "Lightning Sword", 7)
    revive = Potion(3, 2, "Revive", 7)
    full_team_revive = Potion(3, 2, "Full Team Revive", 7)

    # Enchants the revive to have a greater magic_level
    revive.enchant(2)

    # Prints out each magic_level, which is now increased
    # for
    print(lightning_sword.magic_level)
    print(revive.magic_level)
    print(full_team_revive.magic_level)

    # Creates a 'party_bag' with a weight and size limit of 15 each
    # and adds three separate items
    party_bag = Bag(15, 15)
    party_bag.add(Potion(1, 1, "Healing Potion", 2))
    party_bag.add(Weapon(4, 3, "Dagger", 1))
    party_bag.add(Weapon(6, 5, "Axe", 3))

    # The 'party' is a list of three strings
    party = ['Cleric', 'Knight', 'Berserker']
    # Set up empty dictionary
    party_dict = {}
    # Initialize for loop
    for party_member in party:
        # Update dictionary with each different item in the Bag
        party_dict[party_member] = party_bag.inventory()[party.index(party_member)] # [1]

    # Prints out resulting dictionary
    print(party_dict)

# Calling main function
if __name__ == "__main__":
    main()