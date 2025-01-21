def find_kth_character(S, K):
    i=0
    while i<len(S):
        # Find the substring
        substring = ""
        while i<len(S) and S[i].isalpha():
            substring += S[i]
            i += 1
            
        # Find the frequency
        freq = 0
        while i < len(S) and S[i].isdigit():
            freq = freq * 10 + int(S[i])
            i += 1
            
        # Calculate the resultant length
        result_length  = len(substring)*freq
        
        if K <= result_length:
            # Kth character lies in this substring
            return substring[(K-1)%len(substring)]
        
        # Update K for the next part of the string
        K -= result_length
        
    return "" # Return empty if K is out of bounds

# Function to take input and execute the program
def take_input_and_execute():
    S = input("Enter the encrypted string: ")
    K = int(input("Enter the value of K: "))
    result = find_kth_character(S, K)
    print(f"The Kth character is: {result}")
    
# Main function
def main():
    take_input_and_execute()
    
if __name__=="__main__":
    main()