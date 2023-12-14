vowels = 'aeiou'
ip_str = "Guvi Geeks network private limited"
ip_str = ip_str . casefold()
count = {}. fromkeys(vowels, 1)
for char in ip_str:
    if char in count:
        count[char] += 1
print(count)
