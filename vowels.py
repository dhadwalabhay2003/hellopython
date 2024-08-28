def count_vowels(string_list):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Initialize total vowel count
    total_vowels = 0
    
    # Iterate through each string in the list
    for string in string_list:
        # Initialize count for each string
        count = 0
        # Count vowels in the current string
        for char in string:
            if char in vowels:
                count += 1

        total_vowels += count
    return total_vowels

# Example usage
string_list = ["hello", "world", "python", "programming"]
print(count_vowels(string_list))
