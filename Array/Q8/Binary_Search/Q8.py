def search_rotated_array(arr, target):
    """
    Perform binary search on a rotated sorted array to find the target value.

    Parameters:
    arr (list): Rotated sorted array.
    target (int): Value to search for.

    Returns:
    int: Index of the target if found, otherwise -1.
    """
    start=0
    end = len(arr) - 1
    
    while start < end:
        mid = (start + end) // 2
        
        # Check if the mid element is the target
        if arr[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]: # target lies in the left half
                end = mid - 1
            else:
                start = mid + 1
        else:
            # The right half is sorted
            if arr[mid] < target <= arr[end]: # Target lies in the right half
                start = mid+1
            else:  # Target lies in the left half
                end = mid - 1
                
    # Target not found
    return -1


def take_input():
    """
    Take input for the rotated sorted array and the target value.
    """
    print("Enter the rotated sorted array elements (space-separated):")
    arr = list(map(int, input().split()))
    print("Enter the value to search: ")
    target = int(input())
    return arr, target


def main():
    """
    Main function to execute the search in a rotated sorted array.
    """
    arr, target = take_input()
    result = search_rotated_array(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
        
if __name__=="__main__":
    main()
    
            