try:
     n=int(input("enter the number:"))
except:
    ValueError
    print("enter the proper value")
else:
    if(n<=0):
        print("invalid")
    for i in range(1,n):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print("")
