def longest_common_substring(str1, str2):
    # Initialize a 2D list to store lengths of longest common suffixes
    m = len(str1)
    n = len(str2)
    lcsuff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    length = 0  # Length of longest common substring
    end_index = 0  # Ending index of longest common substring in str1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcsuff[i][j] = lcsuff[i - 1][j - 1] + 1
                if lcsuff[i][j] > length:
                    length = lcsuff[i][j]
                    end_index = i
            else:
                lcsuff[i][j] = 0

    # Longest common substring is from index end_index-length to end_index-1 in str1
    start_index = end_index - length
    return str1[start_index:end_index]


# Example usage
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = longest_common_substring(str1, str2)
print(f"Longest common substring: {result}")
