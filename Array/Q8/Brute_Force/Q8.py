def linearSearch(arr, target):
    """
    Perform a linear search to find the target in the array.
    
    Parameters:
    arr (list): List of elements.
    target (int): Value to search for.
    
    Returns:
    int: Index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
        
    return -1

def take_input():
    """
    Take input for the array and the target value.
    """
    print("Enter the array elements (space-separated):")
    arr = list(map(int, input().split()))
    print("Enter the value to search:")
    target = int(input())
    return arr, target

def main():
    """
    Main function to execute the linear search.
    """
    arr, target = take_input()
    result = linear_search(arr, target)
    if result != 1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
        
if __name__=="__main__":
    main()