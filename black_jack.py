def blackjack(a,b,c):
    result=a+b+c
    if  result<=21 :
        return result
    elif result>21 and a==11 or b==11 or c ==11:
        return result-10
    else:
        return "BUST"


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))