import string

def panagram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    str1=str1.replace(" ","").lower()
    str1=set(str1)
    return str1==alphaset
print(panagram("The quick brown fox jumps over the lazy dog"))