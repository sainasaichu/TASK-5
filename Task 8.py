def is_anagram(a,b) :
    if sorted(a) == sorted(b) :
        return True
    return False
print(is_anagram("Asia" , "aiAs"))