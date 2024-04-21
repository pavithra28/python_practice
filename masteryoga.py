def master_yoda(text):
    st=text.split()
    return " ".join(st[::-1])
print(master_yoda('I am home'))
print(master_yoda('We are ready'))