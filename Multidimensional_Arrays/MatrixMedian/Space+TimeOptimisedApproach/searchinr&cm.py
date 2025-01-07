def take_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix, rows, cols

def count_elements_less_equal(row, target):
    # Use binary search to find the count of elements less than or equal to the target in a sorted row.    
    low, high = 0, len(row)
    while low < high:
        mid = (low+high)//2
        if row[mid] <= target:
            low = mid+1
        else:
            high=mid
    return low

def find_median(matrix, rows, cols):
    MIN = matrix[0][0]
    MAX = matrix[-1][-1]
    
    low, high = MIN, MAX
    
    while low<high:
        mid = (low + high) // 2
        count = 0
        
        # count elements <= mid
        for row in matrix:
            count += count_elements_less_equal(row, mid)
            
        if count <= (rows*cols)//2:
            low = mid+1
        else:
            high = mid
            
    return low

def main():
    matrix, rows, cols = take_input()
    median = find_median(matrix, rows, cols)
    print(f"The median of the matrix is: {median}") 
    

if __name__=="__main__":
    main()    
    