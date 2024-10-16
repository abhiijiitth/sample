n=int(input("enter a number"))
if n<10:
    price=120
elif n>=10 and n<=99:
    price=85
else :
    price=70
cost=n*price
print(cost)
