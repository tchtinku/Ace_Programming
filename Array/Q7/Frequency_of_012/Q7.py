def sort_array_by_counting(arr):
    """
    Function to sort an array containing only 0s, 1s, and 2s using a counting approach.
    """
    # Count frequencies of 0s, 1s and 2s
    count_0, count_1, count_2 = 0, 0, 0
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1
            
    # Overwrite array based on counts
    index = 0
    for _ in range(count_0):
        arr[index] = 0
        index += 1
    for _ in range(count_1):
        arr[index] = 1
        index += 1
    for _ in range(count_2):
        arr[index] = 2
        index += 1
        
    return arr

def take_input():
    """
    Function to take input from the user.
    """
    print("Enter the array elements (only 0s, 1s and 2s, space-separated):")
    arr = list(map(int, input().split()))
    return arr

def main():
    """
    Main function to execute the program.
    """
    arr = take_input()
    print("Sorted array: ", sort_array_by_counting(arr))
    
if __name__=="__main__":
    main()        
    