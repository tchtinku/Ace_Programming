def take_input():
    str = input("Enter the string (str): ")
    ptr = input("Enter the pattern (ptr): ")
    return str, ptr

def find_anagrams_sliding_window(str, ptr):
    n, m = len(str), len(ptr)
    if m>n:   # If pattern length is greater than string, no anagrams possible
        return []
    
    # Frequency maps for str and ptr
    strMap = [0]*26
    ptrMap = [0]*26
    result = []
    
    # Build frequency map for str
    for ch in ptr:
        ptrMap[ord(ch) - ord('a')] += 1
        
    # Build initial window in str
    for i in range(m):
        strMap[ord(str[i]) - ord('a')] += 1
        
    # Check if the initial window is an anagram
    if strMap == ptrMap:
        result.append(0)
        
    # Sliding Window
    for i in range(m, n):
        # Remove the character going out of window
        strMap[ord(str[i - m]) - ord('a')] -= 1
        # Add the character coming into the window
        strMap[ord(str[i]) - ord('a')] += 1
        # Check if the current window is an anagram
        if strMap == ptrMap:
            result.append(i-m+1)
            
    return result

def main():
    str, ptr = take_input()
    result = find_anagrams_sliding_window(str, ptr)
    print(f"Starting indices of anagrams of '{ptr}' in '{str}': {result}")
    
if __name__=="__main__":
    main()