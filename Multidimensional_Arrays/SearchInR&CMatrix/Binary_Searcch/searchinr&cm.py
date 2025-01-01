def binary_search_in_matrix(matrix, target):
    """
    Search for target element in a sorted 2D matrix using binary search.
    
    Parameters:
    matrix (list of lists): 2D list representing the matrix (rows sorted).
    target (int): The element to search for.
    
    Returns:
    tuple: The position of the target as (row, column) or (-1, -1) if not found.
    """
    for row in range(len(matrix)):
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return row, mid
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid+1
    return -1, -1

def take_input():
    """
    Take input for the matrix and the target element.
    
    Returns:
    tuple: The matrix and the target element.
    """
    n = int(input("Enter the number of rows and columns in the quare matrix: "))
    print("Enter the element of the matrix row by row (sorted in each row):")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    target = int(input("Enter the target element to search for: "))
    return matrix, target


def main():
    """
    Main function to search for a target element in the matrix.
    """
    matrix, target = take_input()
    position = binary_search_in_matrix(matrix, target)
    if position == (-1, -1):
        print("Element not found in the matrix.")
    else:
        print(f"Element found at position: {position}")
        
if __name__=="__main__":
    main()