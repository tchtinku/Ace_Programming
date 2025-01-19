def take_input():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return str1, str2

def min_anagram_diff(str1, str2):
    # Initialize count for minimum anagram difference
    minAnagramDiff = 0
    str2 = list(str2)   # convert str2 to a list for mutability
    
    for char in str1:
        found = False
        for i in range(len(str2)):
            if str2[i] == char:
                str2[i] = '#'  # Mark the character as used
                found = True
                break
        if not found:
            minAnagramDiff += 1   # Increment count if character not found
            
    return minAnagramDiff

def main():
    str1, str2 = take_input()
    if len(str1) != len(str2):
        print("Strings must be of equal length to compare anagrams.")
        return
    
    result = min_anagram_diff(str1, str2)
    print(f"Minimum number of changes to make the strings anagrams: {result}")
    
if __name__=="__main__":
    main()