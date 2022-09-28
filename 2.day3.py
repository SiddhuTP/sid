def sqrsumevenNsumodd(s):
    odd=0
    even=0
    for i in s:
        if (i%2==0):
            even=even+i**2
        else:
            odd=odd+i**2
    s=[odd,even]
    return s
s=[]
e=int(input("enter the number of elements:"))
if e<=0:
    print("invalid input")
for i in range(e):
    if e<0:
      print("invalid input")
    sel=int(input("enter the element:"))
    s.append(sel)
print(sqrsumevenNsumodd(s))                  
            
