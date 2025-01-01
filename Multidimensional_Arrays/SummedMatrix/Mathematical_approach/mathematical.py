def count_occurrences(n, q):
    """
    Calculate the number of occurrences of the number q in the diagonal pattern matrix.
    
    Parameters:
    n (int): Size of the square matrix (N*N)
    q (int): The query number whose occurrences need to be counted.
    
    Returns:
    int: The count of occurrences of the number q.
    """
    if q <= 1+n:
        return q-1
    else:
        return 2*n-q+1
    
def take_input():
    """
    Take input for the size of the matrix and the query number.
    
    Returns:
    tuple: The size of the matrix (n) and the query number (q). 
    """
    n = int(input("Enter the size of the square matrix (N): "))
    q = int(input("Enter the query number (q): "))
    
def main():
    """
    Main function to calculate and print the occurrences of the query number q in the matrix.
    """
    n, q = take_input()
    result = count_occurrences(n, q)
    print(f"The number {q} occurs {result} times in the matrix." )
    
if __name__=="__main__":
    main()