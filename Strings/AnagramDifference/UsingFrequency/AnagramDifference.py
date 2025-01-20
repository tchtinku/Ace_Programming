def take_input():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return str1, str2

def min_anagram_manipulations(str1, str2):
    if len(str1) != len(str2):
        return "Strings must be of equal length to make them anagrams."
    
    freq = [0]*26  # Array to store character frequencies
    
    # Update frequencies based on str1
    for char in str1:
        freq[ord(char) - ord('a')] += 1
        
    # Update frequencies based on str2
    for char in str2:
        freq[ord(char) - ord('a')] -= 1
        
        
    # Calculate the sum of absolute differences
    freqDiff = sum(abs(x) for x in freq)
    
    # Minimum manipulations to make the strings anagrams
    return freqDiff // 2

def main():
    str1, str2 = take_input()
    result = min_anagram_manipulations(str1, str2)
    print(f"Minimum manipulations required to make the strings anagrams: {result}")
    
if __name__=="__main__":
    main()