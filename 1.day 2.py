try:
    l=[]
    n1=int(input("enter how many inputs: "))
    m=int(input("Enter the m value"))
    n=int(input("Enter the n value"))
    for i in range(n1):
        a=int(input("enter element: "))
        l.append(a)
    l.sort()
    print("sorted list",l)
    a=l[-m]
    b=l[n-1]
    print("maximum number: ",a)
    print("minimum number: ",b)
    print("sum= ",a+b)
    print("difference= ",a-b)
except IndexError:
    print("enter the proper m and n value")
