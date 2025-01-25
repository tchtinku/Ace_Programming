def take_input():
    string = input("Enter the string: ")
    return string

def find_min_length_substring(string):
    # Step 1: Find all distinct characters
    distinct_chars = set(string)
    distCount = len(distinct_chars)
    
    # Step 2: Initialize variables
    start, end = 0, 0
    count = 0
    frequency = {}
    minLength = len(string)
    startIndex = 0
    
    # Step 3: Sliding window technique
    while end < len(string):
        # Expand the window
        char = string[end]
        frequency[char] = frequency.get(char, 0) + 1
        if frequency[char] == 1:
            count += 1
            
        # Shrink the window
        while count == distCount:
            if end - start + 1 < minLength:
                minLength = end - start + 1
                startIndex = start
                
            # Remove the start character from the window
            frequency[string[start]] -= 1
            if frequency[string[start]] == 0:
                count -= 1
            start += 1
            
        end += 1
        
    # Return the minimum length substring
    return string[startIndex:startIndex + minLength], minLength

def main():
    string = take_input()
    result, length = find_min_length_substring(string)
    print(f"The minimum length substring containing all distinct characters is: '{result}' with length {length}")
    
if __name__=="__main__":
    main()