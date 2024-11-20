def are_interval_non_overlapping(intervals):
    n = len(intervals)
    for i in range(n):
        for j in range(i+1, n):
            # Check if intervals[i] & intervals[j] overlap
            if not (intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]):
                return False
    return True

def take_input():
    print("Enter the number of intervals: ")
    n = int(input())
    intervals = []
    print("Enter each interval as start and end values (space-separated):")
    for _ in range(n):
        interval = list(map(int, input().split()))
        intervals.append(interval)
    return intervals

def main():
    intervals = take_input()
    result = are_interval_non_overlapping(intervals)
    if result:
        print("The intervals are non-overlapping")
    else:
        print("The intervals are overlapping")
        
if __name__=="__main__":
    main()