def take_input():
    rows = int(input("Enter number of rows (n): "))
    cols = int(input("Enter number of cols (m): "))
    print("Enter the matrix element row by row: ")
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    k = int(input("Enter the value of k: "))
    return matrix, rows, cols, k


def find_kth_element(matrix, n, m, k):
    startRow, startCol = 0, 0
    count = 0
    
    while startRow < n and startCol < m:
        # Traverse the top row
        for i in range(startCol, m):
            count += 1
            if count == k:
                return matrix[startRow][i]
            
        startRow += 1
        
        # Traverse the right column
        for i in range(startRow, n):
            count += 1
            if count == k:
                return matrix[i][m-1]
        m -= 1
        
        # Traverse the bottom row
        if startRow < n:
            for i in range(m-1, startCol-1, -1):
                count += 1
                if count == k:
                    return matrix[n-1][i]
            n -= 1
            
        # Traverse the left column
        if startCol < m:
            for i in range(n-1, startRow-1, -1):
                count+=1
                if count == k:
                    return matrix[i][startCol]
            startCol += 1
            
    return "k is out of range."


def main():
    matrix, n, m, k = take_input()
    result = find_kth_element(matrix, n, m, k)
    print(f"The {k}-th element in the spiral order traversal is: {result}")
    
if __name__=="__main__":
    main()