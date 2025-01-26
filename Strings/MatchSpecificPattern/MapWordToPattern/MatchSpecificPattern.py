def take_input():
    n = int(input("Enter the number of words: "))
    words = []
    for _ in range(n):
        words.append(input(f"Enter word { _ + 1}: "))
    pattern = input("Enter the pattern: ")
    return words, pattern

def is_valid_match(word, pattern):
    mapPat = {}
    mapWord = {}
    
    for chP, chW in zip(pattern, word):
        if chP not in mapPat and chW not in mapWord:
            mapPat[chP] = chW
            mapWord[chW] = chP
        elif mapPat.get(chP) != chW or mapWord.get(chW) != chP:
            return False
    return True

def find_matching_words(words, pattern):
    valid_words = []
    for word in words:
        if len(word) == len(pattern) and is_valid_match(word, pattern):
            valid_words.append(word)
    return valid_words

def main():
    words, pattern = take_input()
    result = find_matching_words(words, pattern)
    print(f"Words matching the pattern '{pattern}': {result}")
    
if __name__=="__main__":
    main() 