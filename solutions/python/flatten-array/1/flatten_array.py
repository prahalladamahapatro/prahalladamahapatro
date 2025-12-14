#result = []            # Don't declare the list globally, because all the test cases will use the same list, and
                        # We can't refresh/clear the list after the return statement. So, it is better to write inside.
def flatten(iterable):
    result = []            #declare the list here
    # Create a recursive function to check whether the element is an iterator or not.
    def flat(items):
        for item in items:
            if isinstance(item, list):    #call recursively for iterators
                flat(item)
            elif item == None:            # skip the item if it is NONE
                continue
            else:                         # Else, add the item into the return list
                result.append(item)

    flat(iterable)
    return result