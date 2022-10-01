a=int(input("Enter no of rows in matrix1:"))
e=int(input("Enter no of columns in matrix1:"))
h=[]
for i in range(a):
    b=[]
    for j in range(e):
        c=int(input("Enter element matrix1 :"))
        b.append(c)
    h.append(b)
a1=int(input("Enter no of rows in matrix1:"))
e1=int(input("Enter no of columns in matrix1:"))
h1=[]
for i in range(a1):
    b1=[]
    for j in range(e1):
        c1=int(input("Enter element matrix1 :"))
        b1.append(c1)
    h1.append(b1)
print("MATRIX 1:")
for i in range(a):
    for j in range(e):
        print(h[i][j],end=" ")
    print()
print("MATRIX 2:")
for i in range(a1):
    for j in range(e1):
        print(h1[i][j],end=" ")
    print()
if(a!=a1 or e!=e1):
    print("Same no of rows and column can be added")
else:
    d=[]
    for i in range(a):
        d1=[]
        for j in range(e):
            n=h[i][j]+h1[i][j]
            d1.append(n)
        d.append(d1)
    print("Added matrix :")
    for i in range(a):
        for j in range(e):
            print(d[i][j],end=" ")
        print()
