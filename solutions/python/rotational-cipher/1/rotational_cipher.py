def rotate_char(c, key):
    if 'a' <= c <= 'z':
        # Subtract the ord('a') from the ord(char), then find the remainder after adding the key, then add ord('a')
        start = ord('a')
        return chr((ord(c) - start + key) % 26 + start)
    elif 'A' <= c <= 'Z':
        start = 65
        return chr((ord(c) - start + key) % 26 + start)
    else:
        return c

def rotate(text, key):
    key = key % 26  # handle keys outside 0–26 just in case
    return ''.join(rotate_char(c, key) for c in text)