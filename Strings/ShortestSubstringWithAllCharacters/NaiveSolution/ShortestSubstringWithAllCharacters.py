def find_min_length_substring(s):
    from collections import Counter
    
    # Step 1: Count distinct characters in the string
    distinct_chars = set(s)
    total_distinct = len(distinct_chars)
    
    n = len(s)
    min_length = float('inf')  # To store the minimum length of a valid substring
    result = ""  # To store the result substring
    
    # Step 2: Generate substrings using two pointers
    for i in range(n):
        # Initialize a hashmap to count characters in the current substring
        current_count = Counter()
        count = 0
        
        for j in range(i, n):
            char = s[j]
            current_count[char] += 1
            
            # If this character is encountered for the first time, increment count
            if current_count[char] == 1:
                count += 1
                
            # Step 4: Check if substring is valid
            if count == total_distinct:
                current_length = j-i+1
                
                if current_length < min_length:
                    min_length = current_length
                    result = s[i:j+1]
                break   # No need to expand further for this starting point
            
            
    return result, min_length

# take input function
def take_input():
    s = input("Enter the string: ")
    return s

# main function
def main():
    s = take_input()
    result, length = find_min_length_substring(s)
    print(f"The minimum length substring containing all distinct characters is: 'result' with length {length}")
    
if __name__=="__main__":
    main()