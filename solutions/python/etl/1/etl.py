'''
legacy data is a dict that stores the points as a key, and the alphabets as list.
Now, create a data dict, store the alphabet in lowercase as key, and the points as value.
'''
def transform(legacy_data):
    data = {}
    for key, val in legacy_data.items():
        for item in val:
            data[item.lower()] = key

    return data