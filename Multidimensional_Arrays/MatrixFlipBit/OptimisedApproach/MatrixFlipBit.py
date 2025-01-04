def count_flipped_bits(matrix):
    """
    Count the number of 1s in the same row or column as any 0 in the matrix,
    ensuring rows and columns are not rechecked using visited arrays.
    
    Parameters:
    matrix (list of lists): Input 2D binary matrix.
    
    Returns:
    int: Count of 1s to be flipped. 
    """
    n = len(matrix)
    visitedRow = [False]*n
    visitedCol = [False]*n
    zeroPositions = []
    
    # Step 2: Locate all 0s in the matrix
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroPositions.append((i, j))
                
    count = 0
    
    # Step 3: Process rows and cols of all 0s
    for i, j in zeroPositions:
        # check if the row is already visited
        if not visitedRow[i]:
            # Traverse the row
            for col in range(n):
                if matrix[i][col] == 1:
                    count += 1
                    matrix[i][col] = -1
            visitedRow[i] = True
            
        # Check if the column is already visited
        if not visitedCol[j]:
            # Traverse the column
            for row in range(n):
                if matrix[row][j] == 1:
                    count += 1
                    matrix[row][j] = -1
            visitedCol[j] = True
            
    return count

def take_input():
    """
    Take input for the binary matrix.
    
    Returns:
    list of lists: Binary Matrix.
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
    print("Input Matrix: ")
    for row in matrix:
        print(" ".join(map(str, row)))
        
    result = count_flipped_bits(matrix)
    print("Count of 1s to be flipped:", result)
    
if __name__=="__main__":
    main()