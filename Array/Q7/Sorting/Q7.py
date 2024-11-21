def sort_array(arr):
    """
    Function to sort the array.
    Uses Python's inbuilt sort function.
    """
    arr.sort()   # Inbuilt sort function, time complexity O(N*log(N))
    return arr

def take_input():
    """
    Function to take input from the user.
    """
    print("Enter the size of the array:")
    n = int(input())
    print("Enter the array elements (space-separated):")
    arr = list(map(int, input().split()))
    return arr

def main():
    """
    Main function to execute the program.
    """
    arr = take_input()
    print("Sorted Array:", sort_array(arr))
    
if __name__=="__main__":
    main()