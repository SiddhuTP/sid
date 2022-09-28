def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
try:
    a=int(input("enter the no:"))
    if(a<=0):
        print("invalid input")
    else:
        print("factorial:",fact(a))
        c=0
        for i in range(1,a+1):
            if(a%i==0):
                c+=1
        print("no of factors:",c)
except ValueError:
    print("invalid input")
