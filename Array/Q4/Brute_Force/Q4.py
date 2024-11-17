def max_area_brute_force(height):
    n = len(height)
    global_max = float('-inf') # Initialize to a very small value
    
    # Iterate over all pairs of lines
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the current area
            current_area = (j-i)*min(height[i], height[j])
            
            # Update the global maximum area if necessary
            global_max = max(global_max, current_area)
            
    return global_max


def take_input():
    # Take input for heights
    print("Enter the heights of the lines (space-separated):")
    height = list(map(int, input().split()))
    return height

def main():
    height = take_input()
    result = max_area_brute_force(height)
    print("Maximum water that can be contained:", result)
    
if __name__=="__main__":
    main()