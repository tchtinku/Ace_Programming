def take_input():
    # Input size of matrix and number of tasks
    N = int(input("Enter the size of the matrix (N): "))
    K = int(input("Enter the number of tasks (K):"))
    tasks = []
    print("Enter each task as a pair (i, j): ")
    
    for _ in range(K):
        i, j = map(int, input().split())
        tasks.append((i, j))
    return N, K, tasks

def process_tasks(N, K, tasks):
    # Initialize Variables
    rows, cols = N, N
    rowSet, colSet = set(), set()
    outputArray = []
    
    for i, j in tasks:
        # Eliminate the row if not already eliminated
        if i not in rowSet:
            rowSet.add(i)
            rows -= 1
        
        # Eliminate the column if not already eliminated
        if j not in colSet:
            colSet.add(j)
            cols -= 1
            
            
        # Calculate the number of empty cells
        empty_cells = rows * cols
        outputArray.append(empty_cells)
        
    return outputArray

def main():
    N, K, tasks = take_input()
    result = process_tasks(N, K, tasks)
    print("Output Array:", result)
    
if __name__=="__main__":
    main()
    