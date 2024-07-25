# function that takes a string and returns the number of unique characters in it.
s = "Guvi geeks network private limited"
d = {}
for i in s:
    d[i] = 0
for i in s:
    d[i] = d[i]+1
print(d)
for i in s:
    if (d [i] == 1) :
        print(i)
