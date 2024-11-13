def find_min_subarray_with_k_distinct(arr, k):
    n = len(arr)
    freq_map = {}
    min_len = float("inf")
    start = 0
    result = (-1, -1)
    
    i=0
    for j in range(n):
        # Add element at the end of the window
        freq_map[arr[j]] = freq_map.get(arr[j], 0) + 1
        
        # Check if we have exactly k distinct elements in the window
        while len(freq_map) == k:
            # Update minimum length and result indices if this subarray is shorter
            if (j - i + 1) < min_len:
                min_len = j-i+1
                result(i, j)
                
            # Shrink the window from the start
            freq_map[arr[i]] -= 1
            if freq_map[arr[i]] == 0:
                del freq_map[arr[i]]
            i += 1
            
    if result == (-1, -1):
       return -1 # No subarray with exactly K distinct elements
    else:
       return arr[result[0]: result[1] + 1]  # Return the smallest subarray

def take_input():
    arr = list(map(int, input("Enter the array elements: ").split()))
    k = int(input("Enter the value of K (distinct elements): "))
    return arr, k

def main():
    arr, k = take_input()
    result = find_min_subarray_with_k_distinct(arr, k)
    if result == -1:
        print("No subarray with exactly", k, "distinct elements")
    else:
        print("Smallest subarray with exactly", k, "distinct elements: ", result)
        
if __name__=="__main__":
    main()
