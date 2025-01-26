def take_input():
    str = input("Enter the string (str): ")
    ptr = input("Enter the pattern (ptr): ")
    return str, ptr

def find_anagrams(str, ptr):
    n, m = len(str), len(ptr)
    result = []
    sorted_ptr = sorted(ptr)    # Precomputed the sorted pattern
    
    for i in range(n - m + 1):     # Iterate over all possible starting indices
        substring = str[i:i + m]    # Extract substring of length m
        if sorted(substring) == sorted_ptr:   # Check if sorted substring equals sorted_ptr
            result.append(i)
            
    return result

def main():
    str, ptr = take_input()
    result = find_anagrams(str, ptr)
    print(f"Starting indices of anagrams of '{ptr}' in '{str}': {result}")
    
if __name__=="__main__":
    main()