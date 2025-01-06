def rotate_row(row, k):
    """
    Rotates a single row of the matrix by k steps to the right.
    """
    n = len(row)
    k = k % n  # Handle cases where k > n
    # Reverse the entire row
    row.reverse()
    # Reverse the first k elements
    row[:k] = reversed(row[:k])
    # Reverse the remaining n-k elements
    row[k:] = reversed(row[k:])
    return row

def rotate_matrix_rows(matrix, k):
    """
    Rotates each row of the matrix by k steps to the right.

    Parameters:
    matrix (list of lists): The input matrix to rotate.
    k (int): Number of steps to rotate each row to the right.

    Returns:
    list of lists: The rotated matrix.
    """
    rotated_matrix = []
    for row in matrix:
        rotated_matrix.append(rotate_row(row.copy(), k))
    return rotated_matrix

def take_input():
    """
    Take input for the matrix and the number of rotations.
    
    Returns:
    tuple: The matrix and the number of rotations.
    """
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    print("Enter the elements of the matrix row by row:")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    k = int(input("Enter the number of rotations: "))
    return matrix, k

def main():
    """
    Main function to rotate each row of the matrix.
    """
    matrix, k = take_input()
    result = rotate_matrix_rows(matrix, k)
    print("Rotated Matrix:")
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
