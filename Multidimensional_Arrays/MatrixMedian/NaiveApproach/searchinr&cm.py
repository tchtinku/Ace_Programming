def find_median(matrix, N, M):
    """
    Function to find the median of a matrix.
    :param matrix: 2D list of integers (matrix)
    :param N: Number of rows in the matrix
    :param M: Number of cols in the matrix
    :return: Median of the matrix
    """
    aux = []
    
    # Add all elements of the matrix to the auxiliary array
    for i in range(N):
        for j in range(M):
            aux.append(matrix[i][j])
            
    # sort the array
    aux.sort()
    
    # Find and return the median
    mid_index = (N*M)//2
    return aux[mid_index]

def take_input():
    """
    Function to take input for a matrix.
    :return: Matrix and its dimensions
    """
    N = int(input("Enter the number of rows (N):"))
    M = int(input("Enter the number of cols (M):"))
    print("Enter the elements of the matrix row by row:")
    matrix = []
    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix, N, M

def main():
    """
    Main function to find and display the median of a matrix
    """
    matrix, N, M = take_input()
    result = find_median(matrix, N, M)
    print(f"The median of the matrix is: {result}")
    
# Run the main function
if __name__=="__main__":
    main()