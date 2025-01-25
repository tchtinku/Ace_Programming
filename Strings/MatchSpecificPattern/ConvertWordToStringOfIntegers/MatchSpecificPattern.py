def take_input():
    n = int(input("Enter the number of words: "))
    words = []
    for _ in range(n):
        words.append(input(f"Enter word {_ + 1}:  "))
    pattern = input("Enter the pattern: ")
    return words, pattern

def generate_hash(word):
    char_map = {}
    hash_value = []
    unique_id = 1
    
    for char in word:
        if char not in char_map:
            char_map[char] = unique_id
            unique_id += 1
        hash_value.append(str(char_map[char]))
        
    return "".join(hash_value)

def find_matching_words(words, pattern):
    pattern_hash = generate_hash(pattern)
    valid_words = []
    
    for word in words:
        if len(word) != len(pattern):
            continue
        if generate_hash(word) == pattern_hash:
            valid_words.append(word)
            
    return valid_words

def main():
    words, pattern = take_input()
    result = find_matching_words(words, pattern)
    print(f"Words matching the pattern '{pattern}': {result}") 
    
if __name__=="__main__":
    main()