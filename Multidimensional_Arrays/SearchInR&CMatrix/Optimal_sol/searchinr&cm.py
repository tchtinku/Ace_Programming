def search_in_sorted_matrix(matrix, target):
    """
    Search for a target element in a sorted 2D matrix starting from the top-right corner.
    
    Parameters:
    matrix (list of lists): 2D lsit representing the matrix (rows and cols sorted).
    target (int): The element to search for.
    
    Returns:
    tuple: The position of the target as (row, col) or (-1, -1) if not found.
    """
    n = len(matrix)
    if n == 0:
        return -1, -1
    
    i, j = 0, n - 1 # Start from top-right corner
    while i < n and j >= 0:
        if matrix[i][j] == target:
            return i, j
        elif matrix[i][j] > target:
            j -= 1   # Move left
        else:
            i += 1
    return -1, -1

def take_input():
    """
    Take input for the matrix and the target element.
    
    Returns:
    tuple: The matrix and the target element.
    """
    n = int(input("Enter the number of rows and cols in the square matrix: "))
    print("Enter the elements of the matrix row by row  (sorted in both rows and cols):")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    target = int(input("Enter the target element to search for: "))
    return matrix, target

def main():
    """
    Main function to search for a target element in the matrix.
    """
    matrix, target = take_input()
    position = search_in_sorted_matrix(matrix, target)
    if position == (-1, -1):
        print("Element not found in the matrix.")
    else:
        print("Element found at position: {position}")
        
if __name__=="__main__":
    main()