def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    elif a%2==0 or b%2==0:
        return max(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))