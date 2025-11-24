def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    new = ""
    for char in sentence.lower():
        if char in alphabets:
            new += char
    new = set(new)
    return len(new) == 26