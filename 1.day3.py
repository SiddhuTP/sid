s=int(input("enter the principle amount:"))
e=10
l=int(input("enter the number of years:"))
m=input("is customer senior citizen(y/n):")
def simpleinterest(s,e,l,m):
    sl=(s*e*l)/100
    if(m=='y'):
        e=12
        print("the simple interest is ",sl)
    elif(s<0):
        print("invalid input")
    elif(l<0):
        print("invalid input")
    else:
        e=10
        print("the simple imterest is",sl)
simpleinterest (s,e,l,m)        
