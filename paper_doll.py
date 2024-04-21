def paper_doll(text):
    out=[]
    for i in text:
        out.append(i*3)
    return  ''.join(out)

print(paper_doll('Hello'))
print(paper_doll('Hiii'))