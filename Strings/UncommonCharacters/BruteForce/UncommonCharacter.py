def take_input():
    s = input("Enter the string:")
    D = int(input("Enter the number of rotations (D): "))
    return s, D


def left_rotate(s, D):
    # Perform left rotation
    D %= len(s)   # Handle cases where D > len(s)
    ans = s[D:] + s[:D]
    print(f"Left rotated string: {ans}")
    return ans

def right_rotate(s, D):
    # Perform right rotation
    D %= len(s)  # Handle cases where D > len(s)
    ans = s[-D:]+s[:-D]
    print(f"Right rotated string: {ans}")
    return ans

def main():
    s, D = take_input()
    print("\n Performing rotations...")
    left_rotate(s, D)
    right_rotate(s, D)
    
if __name__=="__main__":
    main()