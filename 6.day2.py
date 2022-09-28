def items(n):
    a=200*(n-1)
    return a
b=int(input("enter the no:"))
if(b>=0):
    print("no of items:",b)
    print("shipping charge:",items(b)+750)
else:
    print("Invalid input")
