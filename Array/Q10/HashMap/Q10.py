############# Majority Element 

def find_majority_element(arr):
    """
    Function to find the majority element using a hashmap.
    
    Parameters:
    arr (list): Input array of integers.
    
    Returns:
    int: Majority element if it exists, otherwise -1.
    """
    n = len(arr)
    freq_map = {}
    
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
        if freq_map[num] > n // 2:
            return num
        
    return -1

def take_input():
    """
    Function to take user input for the array.
    """
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements of the array:")
    arr = [int(input()) for _ in range(n)]
    return arr

def main():
    """
    Main function to find and print the majority element.
    """
    arr = take_input()
    majority_element = find_majority_element()
    if majority_element != -1:
        print(f"The majority element is: {majority_element}")
    else:
        print("No majority element found.")
        
if __name__=="__main__":
    main()