def max_ones_with_flip(arr):
    n = len(arr)
    total_ones = 0
    max_diff = float('-inf')
    
    # Count total ones in the array
    for num in arr:
        if num == 1:
            total_ones += 1
            
    # Traverse all subarrays
    for i in range(n):
        count_one = 0
        count_zero = 0
        for j in range(i, n):
            if arr[j] == 1:
                count_one += 1
            else:
                count_zero += 1
            # Difference between zeroes and ones in subarray
            max_diff = max(max_diff, count_zero - count_one)
            
    # If max_diff remains -inf, the array contains only 1s
    max_diff = max(max_diff, 0)
    
    return total_ones + max_diff

def take_input():
    arr = list(map(int, input("Enter the binary array (space-separated): ").split()))
    return arr

def main():
    arr = take_input()
    result = max_ones_with_flip(arr)
    print("Maximum number of ones after flipping a subarray:", result)

if __name__=="__main__":
    main()    