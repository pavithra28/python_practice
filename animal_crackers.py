def animal_crackers(text):
    st=text.split();
    for i in st:
        if st[0][0]==st[1][0]:
            return True
        else:
            return False
print(animal_crackers('Pavithra Pretesh'))
print(animal_crackers('Vicky Gowtham'))