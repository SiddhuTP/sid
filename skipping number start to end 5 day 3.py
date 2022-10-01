m=int(input("enter the starting number:"))
n=int(input("enter the ending number:"))
c=int(input("enter the skipping number:"))
d=m
while(m>0):
    if(d<n):
        print("skipping numbers:",d)
        d=d+(c+1)
    else:
        break
        
