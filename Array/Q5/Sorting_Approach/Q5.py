def are_intervals_overlapping(intervals):
    # Sort intervals based on the start time
    intervals.sort(key=lambda x:x[0])
    
    # Check for overlaps
    for i in range(1, len(intervals)):
        if intervals[i][0]<intervals[i-1][1]:
            return True # Overlap found
        
    return False # No overlaps found

def take_input():
    print("Enter the number of intervals:")
    n = int(input())
    intervals = []
    print("Enter each interval as start and end values (space-separated):")
    for _ in range(n):
        interval = list(map(int, input().split()))
        intervals.append(interval)
    return intervals

def main():
    intervals = take_input()
    result = are_intervals_overlapping(intervals)
    if result:
        print("The intervals are overlapping.")
    else:
        print("The intervals are non-overlapping.")
        
if __name__=="__main__":
    main()