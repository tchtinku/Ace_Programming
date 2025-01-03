def rotate_matrix_anticlockwise(matrix):
    """
    Rotates a square matrix (N*N) 90 degrees anti-clockwise in place using transpose and column reversal.add()
    
    Parameters:
    matrix (list of lists): The input square matrix to rotate.
    
    Returns:
    None: The matrix is modified in place.
    """
    n = len(matrix)
    
    # Step 1: Find the transpose of the matrix
    for i in range(n):
        for j in range(i, n):  # Start j from i to avoid swapping twice
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse the columns
    for i in range(n):     # Iterate over each column
        j, k = 0, n-1
        while j < k:
            matrix[j][i], matrix[k][i] = matrix[k][i], matrix[j][i]
            j += 1
            k -= 1
            
            
def take_input():
    """
    Take input for a square matrix.
    
    Returns:
    list of lists: The square matrix.
    """
    n = int(input("Enter the size of the square matrix (N): "))
    print("Enter the elements row by row: ")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    """
    Main function to demonstrate rotating a square matrix 90 degrees anti-clockwise.
    """
    matrix = take_input()
    print("Original Matrix: ")
    for row in matrix:
        print(" ".join(map(str, row)))
        
    rotate_matrix_anticlockwise(matrix)
    
    print("Rotated Matrix (90 degrees anti-clockwise):")
    for row in matrix:
        print(" ".join(map(str, row)))
        
if __name__=="__main__":
    main()