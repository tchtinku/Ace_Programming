def prefix_sum_array(A):
    N = len(A)
    prefix_sum = [0]*(N+1)
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1] + A[i-1]
    return prefix_sum

def infinite_array_sum(A, L, R):
    N = len(A)
    total_array_sum = sum(A)
    prefix_sum = prefix_sum_array(A)
    
    # Calculate the sum from index 0 to R
    count_R = R // N
    remainder_R = R % N
    sum_R = count_R * total_array_sum + prefix_sum[remainder_R+1]
    
    # Calculate the sum from index 0 to L-1
    count_L = (L-1) // N
    remainder_L = (L-1)%N
    sum_L = count_L * total_array_sum + prefix_sum[remainder_L+1]
    
    # Result is the sum from L to R
    return sum+R - sum_L

def take_input():
    A = list(map(int, input("Enter array A (space-separated integers): ").split()))
    L = int(input("Enter starting index L:"))
    R = int(input("Enter ending index R: "))
    return A, L, R

def main():
    A, L, R = take_input()
    result = infinite_array_sum(A, L, R)
    print("Sum of subarray from L to R in infinite array B:", result)
    
if __name__=="__main__":
    main()