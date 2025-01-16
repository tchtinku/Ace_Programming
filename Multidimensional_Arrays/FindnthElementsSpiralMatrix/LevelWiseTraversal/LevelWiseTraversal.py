def find_kth_element(matrix, n, m, k):
    startRow, startCol = 0, 0
    while startRow < n and startCol < m:
        # Case 1: kth element in the top row
        if k <= (m - startCol):
            return matrix[startRow][startCol + k - 1]
        
        # Adjust k for top row and move to the next
        k -= (m - startCol)
        n -= 1
        
        # Case 4: kth element in the left column
        if k <= (n-startRow):
            return matrix[n-k][startCol]
        
    return -1 # If k is out of bounds

def take_input():
    print("Enter the number of rows (n) and columns (m):")
    n, m = map(int, input().split())
    print(f"Enter the {n}*{m} matrix:")
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print("Enter the value of k:")
    k = int(input())
    return matrix, n, m, k

def main():
    matrix, n, m, k = take_input()
    result = find_kth_element(matrix, n, m, k)
    if result != 1:
        print(f"The {k}th element in the spiral order is: {result}")
    else:
        print("Invalid k, out of bounds!")
    
if __name__=="__main__":
    main()