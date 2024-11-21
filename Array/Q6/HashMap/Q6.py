def find_pairs_with_sum_hashing(arr, target_sum):
    result = []
    frequency_map = {}
    
    # Iterate through each element in the array
    for num in arr:
        complement = target_sum - num
        
        # Check if the complement exists in the hashmap
        if complement in frequency_map:
            for _ in range(frequency_map[complement]):
                result.append((complement, num))
                
                
        # Update the frequency map for the current number
        frequency_map[num] = frequency_map.get(num, 0)+1
        
    # Sort the result by the first element and then by the second element
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
    pairs = find_pairs_with_sum_hashing(arr, target_sum)
    if pairs:
        print("Pairs with the given sum are: ")
        for pair in pairs:
            print(pair)
    else:
        print("No pairs found with the given sum") 
        
if __name__=="__main__":
    main()