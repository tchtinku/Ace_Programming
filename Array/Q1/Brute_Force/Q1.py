def find_subarray_with_k_distinct_elements(arr, k):
    n = len(arr)
    for i in range(n):
        distinct_elements = set() # Initialize an empty set to store distinct elements
        for j in range(i, n):
            distinct_elements.add(arr[j]) # Add the current element to the set
            if len(distinct_elements) == k: 
                return arr[i:j+1] #Return the subarray with exactly K distinct elements
            elif len(distinct_elements) > k:
                break # Stop searching if we have more than K distinct elements
        if len(distinct_elements) < k:
            break # Stop if fewer elements are left than K
    return -1 # Return -1 if no subarray with exactly K distinct elements is found

def take_input():
    arr = list(map(int, input("Enter the array elements: ").split()))
    k = int(input("Enter the value of K (distinct elements): "))
    return arr, k

def main():
    arr, k = take_input()
    result = find_subarray_with_k_distinct_elements(arr, k)
    if result == -1:
        print("No subarray with exactly", k, "distiinct elements.")
    else:
        print("Subarray with exactly", k, "distinct elements: ", result)
        
if __name__=="__main__":
    main()