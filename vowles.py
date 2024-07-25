# Define the string
input_string = "GIVI GEEKS NETWORK PRIVATE LIMITED"

# Convert the string to uppercase to handle both uppercase and lowercase letters
input_string = input_string.upper()

# Initialize a dictionary to store the count of each vowel
vowel_counts = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

# Iterate over each character in the string
for char in input_string:
    if char in vowel_counts:
        vowel_counts[char] += 1

# Calculate the total number of vowels
total_vowels = sum(vowel_counts.values())

# Print the results
print("Total number of vowels:", total_vowels)
print("Count of each vowel:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
