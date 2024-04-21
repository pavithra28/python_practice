def summer_69(arr):
    sum=0
    add=True
    for i in arr:
        while add:
            if i!=6:
                sum+=i
                break
            else:
                add=False
        while not add:
            if i!=9:
                break
            else:
                add=True
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))