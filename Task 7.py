import collections
s = "abcabcabcd"
c = collections. Counter(s)
print("character counter : " + str(c))
print("most frequent character : " + str(c.most_common(1)))
