def max_area_two_pointer(height):
    n = len(height)
    i, j = 0, n-1 # Start with the widest container
    max_area = 0 # To store the maximum area found
    
    while i<j:
        # Calculate the area of the current container
        current_area = (j-i)*min(height[i], height[j])
        
        # Update max_area if current_area is greater
        max_area = max(max_area, current_area)
        
        # Move the pointer with the smaller height
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
            
    return max_area


def take_input():
    print("Enter the heights of the lines (space-separated):")
    height = list(map(int, input().split()))
    return height

def main():
    height = take_input()
    result = max_area_two_pointer(height)
    print("Maximum water that can be contained:", result)
    
if __name__=="__main__":
    main()