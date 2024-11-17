def max_ones_with_flip(arr):
    n = len(arr)
    total_ones = 0
    curr_max = 0
    max_diff = 0
    
    # Traverse the array
    for i in range(n):
        # Increment total_ones if the current element is 1
        if arr[i] == 1:
            total_ones += 1
            
        # Treat 1 as -1 and 0 as 1 for the difference calculation
        val = -1 if arr[i] == 1 else 1
        
        # Update curr max using the current value
        curr_max = max(val, curr_max+val)
        
        # Update max_diff
        max_diff = max(max_diff, curr_max)
        
    # Return the result
    return total_ones + max_diff

def take_input():
    arr = list(map(int, input("Enter the binary array (space-separated): ").split()))
    return arr

def main():
    arr = take_input()
    result = max_ones_with_flip_optimized(arr)
    print("Maximum number of ones after flipping a subarray:", result)
    
if __name__=="__main__":
    main()