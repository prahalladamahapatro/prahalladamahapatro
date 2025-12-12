def find(search_list, value):
    # Raise a value error if the value is not in the list
    if value not in search_list:
        raise ValueError("value not in array")

    # Return 0 if the list has only a single element
    if len(search_list) == 1:
        return 0

    #Now, check the index of the value in our list USING BINARY SEARCH
    i,j = 0, len(search_list) - 1
    while i <= j:
        mid = (i+j) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            i = mid + 1
        else:
            j = mid - 1