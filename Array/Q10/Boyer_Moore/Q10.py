def find_majority_element(arr):
    """
    Function to find the majority element using the Boyer-Moore Voting Algorithm.
    
    Parameters:
    arr (list): Input array of integers.
    
    Returns:
    int: Majority element if it exists, otherwise -1.
    """
    # Step 1: Find the candidate for majority element
    majority_element = None
    count = 0
    
    for num in arr:
        if count == 0:
            majority_element = num
            count = 1
        elif num == majority_element:
            count += 1
        else:
            count -= 1
            
    # Step 2: Verify if the candidate is the majority element
    count = 0
    for num in arr:
        if num == majority_element:
            count += 1
            
    return majority_element if count > len(arr) // 2 else -1

def take_input():
    """
    Function to take user input for the array.
    """
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements of the array: ")
    arr = [int(input()) for _ in range(n)]
    return arr

def main():
    """
    Main function to find and print the majority element.
    """
    arr = take_input()
    majority_element = find_majority_element(arr)
    if majority_element !=  -1:
        print(f"The majority element is: {majority_element}")
    else:
        print("No majority element found")
        
if __name__=="__main__":
    main()