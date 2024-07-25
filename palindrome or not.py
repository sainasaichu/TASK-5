def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Test the function
test_strings = ["A man, a plan, a canal, Panama", "racecar", "hello", "No lemon, no melon"]
for s in test_strings:
    print(f"'{s}' is a palindrome: {is_palindrome(s)}")
