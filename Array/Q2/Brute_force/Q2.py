def sum_infinite_array(A, L, R):
    N = len(A)
    total_sum = 0
    for i in range(L, R + 1):
        total_sum += A[i%N]
    return total_sum

def take_input():
    A = list(map(int, input("Enter array A (space-separated integers): ").split()))
    L = int(input("Enter starting index L: "))
    R = int(input("Enter ending index R: "))
    return A, L, R

def main():
    A, L, R = take_input()
    result = sum_infinite_array(A, L, R)
    print("Sum of subarray from L to R in infinite array B:", result)
    
if __name__=="__main__":
    main()