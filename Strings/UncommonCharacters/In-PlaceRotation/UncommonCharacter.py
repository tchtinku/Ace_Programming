def take_input():
    s = input("Enter the string: ")
    D = int(input("Enter the number of rotations (D): "))
    return s, D

def reverse_string(s, start, end):
    # Reverse a substring of the string from index `start` to `end`.
    s = list(s)
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

def left_rotate(s, D):
    n = len(s)
    D %= n # Handle cases where D>n
    # Reverse parts of the string as per the algorithm
    s = reverse_string(s, 0, D - 1)
    s = reverse_string(s, D, n - 1)
    s = reverse_string(s, 0, n - 1)
    print(f"Left rotated string: {s}")
    return s

def right_rotate(s, D):
    n = len(s)
    D %= n # Handle cases where D > n
    # Use left rotation logic but compute the effective left rotation as n-D
    return left_rotate(s, n-D)

def main():
    s, D = take_input()
    print("\nPerforming rotations....")
    left_rotate(s, D)
    right_rotate(s, D)
    
if __name__=="__main__":
    main()