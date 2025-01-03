def count_flipped_bits(matrix):
    """
    Count the number of 1s in the same row or column as any 0 in the matrix.
    
    Parameters:
    matrix (list of lists): Input 2D binary matrix.
    
    Returns:
    int: Count of 1s to be flipped.
    """
    n = len(matrix)
    count = 0
    
    for i in range(n):  # Loop through rows
        for j in range(n):     # Loop through columns
            if matrix[i][j] == 0:
                # Check the ith row
                for k in range(n):
                    if matrix[i][k] == 1:
                        count += 1
                        matrix[i][k] = -1    # Mark as visited
                        
                # Check for jth column
                for k in range(n):
                    if matrix[k][j] == 1:
                        count += 1
                        matrix[k][j] = -1  # Mark as visited
                        
    return count

def take_input():
    """
    Take input for the binary matrix.
    
    Returns
    list of lists: Binary Matrix
    """
    n = int(input("Enter the size of the matrix (N): "))
    print("Enter the matrix row by row (space-separated binary values):")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    """
    Main function to demonstrate the counting of flipped bits.
    """
    matrix = take_input()
    print("Input matrix: ")
    for row in matrix:
        print(" ".join(map(str, row)))
        
    result = count_flipped_bits(matrix)
    print("Count of 1s to be flipped:", result)
    
if __name__=="__main__":
    main()
            
        