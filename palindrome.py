def palindrome(s):
    s=s.replace(" ","")
    return s[::-1]==s

print(palindrome('helleh'))
print(palindrome('nurses run'))