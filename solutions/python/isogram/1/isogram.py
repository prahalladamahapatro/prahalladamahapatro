import string as s
def is_isogram(string):
    new = "".join(char for char in string.lower() if char in s.ascii_lowercase)
    return len(new) == len(set(new))
