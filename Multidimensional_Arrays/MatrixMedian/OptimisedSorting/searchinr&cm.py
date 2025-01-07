import heapq

def take_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    print("Enter the matrix row-wise (space-separated): ")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix, rows, cols

def find_median(matrix, rows, cols):
    # Min-heap initialisation
    min_heap = []
    for row in range(rows):
        heapq.heappush(min_heap, (matrix[row][0], row, 0))
        
    count = 0
    median_position = (rows*cols) // 2
    
    while count <= median_position:
        # Extract the minimum element
        value, row, col = heapq.heappop(min_heap)
        count += 1
        
        # If we reach the median position
        if count == median_position + 1:
            return value
        
        # Push the ext element of the same row into the heap
        if col + 1 < cols:
            heapq.heappush(min_heap, (matrix[row][col+1], row, col+1))
            
def main():
    matrix, rows, cols = take_input()
    median = find_median(matrix, rows, cols)
    print(f"he median of the matrix is: {median}")
    
if __name__=="__main__":
    main()