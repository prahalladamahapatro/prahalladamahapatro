"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    items = {}
    return items.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    new = {}
    for recipe in recipe_updates:
        new[recipe[0]] = recipe[1]

    ideas.update(new)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    new = dict(sorted(cart.items()))
    return new


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    #NOTE: we have to send the items which are only present in the cart, not all from the aisle
    new = {}
    for key, value in cart.items():
        if key in aisle_mapping:
            val = [value]
            val = val + aisle_mapping[key]
            new[key] = val

    return dict(reversed(sorted(new.items())))
    #return new
            

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    #NOTE: If the item is present in the cart, then only update the values; else, put as it is
    new = {}
    for key, value in store_inventory.items():
        if key in fulfillment_cart:    
            num = value[0] - fulfillment_cart[key][0]
            if num > 0:
                val = [num] + value[1:]
            else:
                val = ['Out of Stock'] + value[1:]
            new[key] = val
            
        else:
            new[key] = value
    return new