print("Enter * to exit")
a=[]
c,d,e=0,0,0
for i in range(0,100):
   b=input ("Enter a element:") 
   if(b== '*'):
       break
   else:
      a.append(b)
for i in a:
    if(i.isupper()): 
        c+=1
    elif(i.islower()):
        d+=1
    elif(i.isnumeric()):
        e+=1
print("No of lowercase letter=",d)
print("No of uppercase letter=",c) 
print("No of no =",e)
