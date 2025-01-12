def take_count():
    # Input matrix size and tasks
    N = int(input("Enter the size of the matrix (N): "))
    K = int(input("Enter the number of tasks (K): "))
    
    tasks = []
    
    print("Enter each task as a pair (i, j): ")
    
    for _ in range(K):
        i, j = map(int, input().split())
        tasks.append((i, j))
    return N, K, tasks


def count_negative_ones(matrix):
    count = 0
    for row in matrix:
        count += row.count(-1)
    return count

def process_tasks(N, K, tasks):
    # Initialise the matrix with -1
    matrix = [[-1 for _ in range(N)] for _ in range(N)]
    output_array = []
    
    for i, j in  tasks:
        # Replace the ith row with 0
        for col in range(N):
            matrix[i][col] = 0
            
        # Replace jth col with 0
        for row in range(N):
            matrix[row][j] = 0
            
        # Count the number of -1 in the matrix
        count = count_negative_ones(matrix)
        output_array.append(count)
        
    return output_array

def main():
    N, K, tasks = take_input()
    result = process_tasks(N, K, tasks)
    print("Output Array:", result)
    
if __name__=="__main__":
    main()
        