def sort_array_dutch_flag(arr):
    """
    Function to sort an array containing only 0s, 1s, and 2s using the three-pointer approach.
    """
    zeroPos, current, twoPos = 0, 0, len(arr)-1
    
    while current <= twoPos:
        if arr[current] == 0:
            # Swap current and zeroPos, move both pointers forward
            arr[current], arr[zeroPos] = arr[zeroPos], arr[current]
            zeroPos += 1
            current += 1
        elif arr[current] == 1:
            # Move current forward
            current += 1
        else: # arr[current] == 2
            # Swap current and twoPos, move twoPos backward
            arr[current], arr[twoPos] = arr[twoPos], arr[current]
            twoPos -= 1
            
    return arr

def take_input():
    """
    Function to take input from the user.
    """
    print("Enter the array elements (only 0s, 1s, and 2s, space-separated):")
    arr = list(map(int, input().split()))
    return arr

def main():
    """
    Main function to execute the program.
    """
    arr = take_input()
    print("Sorted Array:", sort_array_dutch_flag(arr))
    
if __name__=="__main__":
    main()