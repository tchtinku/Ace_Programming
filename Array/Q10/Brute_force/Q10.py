def find_majority_element(arr):
    """
    Function to find the majority element using brute force.
    
    Parameters:
    arr (list): Input array of integers.
    
    Returns:
    int: Majority element if it exists, otherwise -1.
    """
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                
        if count > n//2:
            return arr[i]
        
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
    majority_element = find_majority_element(arr)
    if majority_element != -1:
        print(f"The majority element is: {majority_element}")
    else:
        print("No majority element found.")
        
if __name__=="__main__":
    main()