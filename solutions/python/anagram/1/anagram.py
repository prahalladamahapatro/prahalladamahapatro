def check(word, anas):
    if sorted(list(word.lower())) == sorted(list(anas.lower())):
        return True
    return False
    
def find_anagrams(word, candidates):
    ana = []
    for anas in candidates:
        # If the word itself comes, or the length of the actual and candidate words are not same.
        if (anas.lower() == word.lower()) or len(word) != len(anas):
            continue
        if check(word, anas):
            ana.append(anas)
    return ana