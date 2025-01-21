def take_input():
    S = input("Enter the encrypted string: ")
    K = int(input("Enter the value of K:"))
    return S, K

def decompress_string(S, K):
    decrypted_string = ""
    i = 0
    n = len(S)
    
    while i<n:
        # Extract the substring of lowercase alphabets
        substring = ""
        while i<n and S[i].isalpha():
            substring += S[i]
            i += 1
            
        # Extract the frequency of the substring
        freq_of_substring = 0
        while i<n and S[i].isdigit():
            freq_of_substring = freq_of_substring * 10 + int(S[i])
            i += 1
            
        # Append the substring freq_of_substring times to the decrypted string
        decrypted_string += substring * freq_of_substring
        
        # If the length of decrypted_string exceeds K, stop early
        if len(decrypted_string) >= K:
            break
        
    # Return the K-th character (1-based index)
    return decrypted_string[K-1] if K <= len(decrypted_string) else None


def main():
    S, K = take_input()
    result = decompress_string(S, K)
    if result:
        print(f"The {K}-th character is: {result}")
    else:
        print("K is larger than the length of the decrypted string.")
        
if __name__=="__main__":
    main()