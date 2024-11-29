def is_symmetric_matrix(matrix):
    """
    Function to check if a square matrix is symmetric using its transpose.
    
    Parameters:
    matrix (list of list of int): Input square matrix.
    
    Returns:
    bool: True if the matrix is symmetric, otherwise False.
    """
    n = len(matrix)
    
    # Step 1: Create transpose of the matrix
    transpose = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpose[i][j] = matrix[j][i]
            
    # Step 2: Compare the original matrix with its transpose
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != transpose[i][j]:
                return False
    return True

def take_input():
    """
    Function to take user input for a square matrix.
    """
    n = int(input("Enter the size of the square matrix (N*N): "))
    print("Enter the elements row by row (space-separated):")
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix

def main():
    """
    Main function to check and print if the matrix is symmetric.
    """
    matrix = take_input()
    if is_symmetric_matrix(matrix):
        print("The matrix is symmetric.")
    else:
        print("The matrix is not symmetric")
        
if __name__=="__main__":
    main()   