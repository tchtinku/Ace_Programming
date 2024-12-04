def is_symmetric_matrix(matrix):
    """
    Check if a given square matrix is symmetric.

    Parameters:
    matrix (list of list of int): Input square matrix.

    Returns:
    bool: True if the matrix is symmetric, False otherwise.
    """
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):    # Traverse the entire matrix
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def take_input():
    """
    Take input for a square matrix from the user.
    
    Returns:
    list of list of int: The input square matrix.
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
        print("Yes, the matrix is symmetric")
    else:
        print("No, the matrix is not symmetric.")
        
if __name__=="__main__":
    main()