def find_pairs_with_sum(arr, target_sum):
    result = []
    n = len(arr)
    
    # Iterate through each pair of elements
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target_sum:
                result.append((arr[i], arr[j]))
                
    # Sort the result by the first element and then by second element
    result.sort(key=lambda x: (x[0], x[1]))
    return result

def take_input():
    print("Enter the size of the array:")
    n = int(input())
    print("Enter the array elements (space-separated):")
    arr = list(map(int, input().split()))
    print("Enter the target sum:")
    target_sum = int(input())
    return arr, target_sum


def main():
    arr, target_sum = take_input()
    pairs = find_pairs_with_sum(arr, target_sum)
    if pairs:
        print("Pairs with the given sum are:")
    else:
        print("No pairs found with the given sum.")
        
        
if __name__=="__main__":
    main()