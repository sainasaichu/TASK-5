# python program to remove the vowels from the string
def remove_vowels(s1):
    output = ''
    for i in s1:
        if i in ('a', 'e', 'i', 'o', 'u'):
            i = ''
            output = output + i
    print(output)
remove_vowels('welcome')