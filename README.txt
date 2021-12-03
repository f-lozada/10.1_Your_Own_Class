GITHUB REPOSITORY LINK: https://github.com/f-lozada/10.1_Your_Own_Class

Item
    This class takes in a weight, size, and name as arguments. Weight and size are expected to be integers, 
    while name is a string. It has one class variable, magic_level, which is set to 0 by default. It has three
    get functions which returns each of the stored parameters, as the data attributes are private and cannot 
    be accessed outside of the class. 
    
    Item also has an item.enchant() method, which takes in itself and increase_magic, which is an integer, 
    as an argument. This increases the magic_level by the specified integer.

    Similarly, item.curse() takes in itself and decrease_magic, which is an integer, as an argument, and
    decreases the magic_level by the specified integer.

Weapon
    Weapon is a class derived from Item. In addition to the weight, size, and name arguments expected of the 
    parent class, it also takes in another integer argument, which its damage attribute. It has a get_damage 
    function, which returns specified damage integer. 

Potion
    Potion is a class derived from Item. In addition to the weight, size, and name arguments expected of the 
    parent class, it also takes in another integer argument, which its healing attribute. It has a get_healing
    function, which returns specified healing integer.

Bag
    This class takes in a size_limit and a weight_limit as arguments, both of which are expected to be integers.
    These arguments are stored as private data attributes, alongside an empty list denoted as self.__items, and
    self.__current_size and self.__current_weight, which by default are 0.  

    The function bag.add() takes in an argument that is an Item. If the current_size and current_weight does not
    exceed the specified size_limit and weight_limit, then the specified item is added to the list in self.__items,
    and the size and weight are added to the current_weight and current_size. If the size_limit and weight_limit
    are exceeded, then the Item will not be added, and an error message will be printed out instead. 

    The function bag.inventory() takes in itself, and returns a list that is the set names of all the Items 
    that are in the bag. 

    The magic method __str__ determines what is displayed when a bag is printed. It displays a string 
    depending on whether the input is an Item, Weapon, or Potion. 

DEMO PROGRAM
    The demo program tests several of the functions associated with the class, such as adding Items to 
    a Bag and enchanting Items. The final part of the program creates a list wih 3 'players' and another 
    Bag that has 3 separate Items, alongside an empty dictionary. Using a for loop, each element in the 
    list is interated through, and the dictionary is updated with the 'players' as the key and each 
    Item in the Bag being separated as their values. 

    The demo program does not need any extraneous files or extra steps to be run by an external user.