def find_triplets_with_zero_sum(arr):
    """
    Function to find all distinct triplets in the array that sum to zero.
    
    Parameters:
    arr (list): Input array of integers.
    
    Returns:
    list: List of all unique triplets that sum to zero.
    """
    n = len(arr)
    result = set()  # To store distinct triplets
    
    # Iterate through the array with three nested loops
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # Check if the triplet sums to zero
                if arr[i]+arr[j]+arr[k] == 0:
                     # Add triplet to set as a sorted tuple
                     result.add(tuple(sorted([arr[i], arr[j], arr[k]])))
                     
    return list(result)

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