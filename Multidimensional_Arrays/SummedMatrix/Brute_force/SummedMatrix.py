def count_cells_with_sum_q(n, q):
    """
    Count the number of cells in a N*N matrix where i+j=q.
    
    Parameters:
    n (int): Size of the square matrix (N*N).
    q (int): Target value for the sum of indices.
    
    Returns:
    int: Total number of cells satisfying i+j=q.
    """
    total = 0
    for i in range(1, n+1):  # Loop for rows
        for j in range(1, n+1):   # Loop for columns
            if i+j == q:
                total += 1
    return total

def take_input():
    """
    Take input for the size of the matrix and the target value q.
    
    Returns:
    tuple: The size of the matrix (n) and the target value (q)
    """
    n = int(input("Enter the size of the square matrix (N): "))
    q = int(input("Enter the target sum value (q): "))
    return n, q

def main():
    """
    Main function to calculate and print the count of cells where i+j = q.
    """
    n, q = take_input()
    result = count_cells_with_sum_q(n, q)
    print(f"The total number of cells where i+j={q} is: {result}")
    
if __name__=="__main__":
    main()