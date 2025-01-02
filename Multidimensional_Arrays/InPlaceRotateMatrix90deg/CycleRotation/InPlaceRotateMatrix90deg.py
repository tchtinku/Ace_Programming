def rotate_matrix_clockwise(matrix):
    """
    Rotates a square matrix (N*N) 90 degrees anti-clockwise in place.
    
    Parameters:
    matrix (list of lists): The input square matrix to rotate.
    
    Returns:
    None: The matrix is modified in place.
    """
    n = len(matrix)
    
    # Process each cycle
    for i in range(n // 2): # Outer to inner cycles
        for j in range(i, n-i-1):
            # Save the top element
            temp = matrix[i][j]
            
            # Move elements from right to top
            matrix[i][j] = matrix[j][n-1-i]
            
            # Move elements from bottom to right
            matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
            
            # Move elements from left to bottom
            matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
            
            # Assign temp to left
            matrix[n-1-j][i] = temp
            
def take_input():
    """
    Take input for a square matrix.
    
    Returns:
    list of lists: The square matrix.
    """
    n = int(input("Enter the size of the square matrix (N): "))
    print("Enter the elements row by row:")
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
    print("Original Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))
        
    rotate_matrix_clockwise(matrix)
    
    print("Rotated Matrix (90 degree anti-clockwise): ")
    for row in matrix:
        print(" ".join(map(str, row)))
        
if __name__=="__main__":
    main()