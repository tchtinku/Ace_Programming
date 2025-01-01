def search_in_matrix(matrix, target):
    """
    Search for a target element in a 2D matrix
    
    Parameters:
    matrix (list of lists): 2D list representing the matrix.
    target (int): The element to search for.
    
    Returns:
    tuple: The position of target as (row, column) or (-1, -1) if not found.
    """
    rows = len(matrix)
    for i in range(rows):
        cols = len(matrix[i])
        for j in range(cols):
            if matrix[i][j] == target:
                return i, j
    return -1, -1

def take_input():
    """
    Take input for the matrix and the target element.add()
    
    Returns:
    tuple: The matrix and the target element.
    """
    n = int(input("Enter the number of rows and columns in the square matrix: "))
    print("Enter the elements of the matrix row by row: ")
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
    position = search_in_matrix(matrix, target)
    if position == (-1, -1):
        print("Element not found in the matrix.")
    else:
        print(f"Element found at position: {position}")
        
if __name__=="__main__":
    main()