b=input("enter the length of string:")
a=[]
e=[]
for i in range(0,b):
    c=input("enter the string")
    a.append(c)
for i in range(0,b):
    d=len(a[i].split())
    e.append(d)
print("LIST =",a)
print("MAX words in a string =",max(e))
