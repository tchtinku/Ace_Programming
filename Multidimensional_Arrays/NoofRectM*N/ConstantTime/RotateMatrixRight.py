def total_rectangles(M, N):
    """
    Function to calculate the total number of rectangles in a grid.
    : param M: Number of rows in the grid
    : param N: Number of cols in the grid
    : return: Total number of rectangles
    """
    return (M*(M+1)*N*(N+1)) // 4

def take_input():
    """
    Function to take user input for the number of rows and columns.
    : return: Value of rows (M) and cols (N)
    """
    M = int(input("Enter the number of rows (M):"))
    N = int(input("Enter the number of cols (N):"))
    
def main():
    """
    Main function to calculate and display the total rectangles in a grid.
    """
    M, N = take_input()
    result = total_rectangles(M, N)
    print(f"The total number of rectangles in a grid with {M} rows and {N} columns is: {result}")
    
# Run the main function
if __name__=="__main__":
    main()
    
