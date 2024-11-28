def find_triplets_with_zero_sum(arr):
    """
    Function to find all distinct triplets in the array that sum to zero using two-pointers.
    
    Parameters:
    arr (list): Input array of integers.
    
    Returns:
    list: List of all unique triplets that sum to zero.
    """
    arr.sort() # Step 1: Sort the array 
    n = len(arr)
    result = []  # To store unique triplets
    
    for i in range(n-2):  # Iterate up to n-2 (as we need triplets)
        if i>0 and arr[i] == arr[i-1]:
            continue # Skip duplicate elements for arr[i]
        
        target = -arr[i]
        front = i + 1
        back = n - 1
        
        while front < back:
            current_sum = arr[front] + arr[back]
            
            if current_sum < target:
                front += 1
            elif current_sum > target:
                back -= 1
            else:
                # Found a triplet   
                result.append((arr[i], arr[front], arr[back]))
                
                # Skip duplicates for arr[front] and arr[back]
                while front < back and arr[front] == arr[front+1]:
                    front += 1
                while front < back and arr[back] == arr[back - 1]:
                    back -= 1
                    
                front += 1
                back -= 1
                
    return result

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
    Main function to find and print triplets with zero sum.
    """
    arr = take_input()
    triplets = find_triplets_with_zero_sum(arr)
    if triplets:
        print("Triplets with zero sum:")
        for triplet in triplets:
            print(triplet)
    else:
        print("No triplets with zero sum found.")
        
if __name__=="__main__":
    main()