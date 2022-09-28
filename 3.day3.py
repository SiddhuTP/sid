a=int(input("enter starting:"))
b=int(input("enter end:"))
c=int(input("number to skip:"))
d=a
while(a>0):
   if(d<b):
       print("skipped numbers:",d)
       d=d+(c+1)
   else:
       break
