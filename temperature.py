temperature=int(input("enter a limit:"))
if temperature<-273.15:
    print("invalid")
elif temperature==-273.15:
    print("0")
elif temperature>-273.15 and temperature<=0:
    print("below freezing")
elif temperature==0:
    print("freezing point")
elif temperature>0 and temperature<100:
    print("normal range")
elif temperature==100:
    print("boiling point")
else:
    print("boiling point")
