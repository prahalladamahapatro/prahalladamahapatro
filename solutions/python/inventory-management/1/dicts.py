"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    count_of_item = {}
    for item in items:
        if item in count_of_item:
            count_of_item[item] += 1
        else:
            count_of_item[item] = 1

    return count_of_item


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        # first check whether the item is available in the dict or not, if available, then deduct 1.
        if item in inventory.keys() and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    #return inventory.pop(item,'')  #don't write like this, because pop() will return the value of                                     key, but we have to return the dictionary after removing the key
    inventory.pop(item,'')    #use default value to avoid KeyError
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    l = []
    for key, value in inventory.items():
        if value > 0:
            l.append((key, value))
    return l

