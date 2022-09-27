a=int(input("Enter a no of fresh loaves purchased :"))
b=int(input("Enter a no of old loaves purchased :"))
if(a<=0):
    print("Enter a positive integer greater than 0")
else:
    f=a*185
    o=(b*185)*60/100
    print("Regular price: Rs.185.00")
    print("Amount of new loaves:", float(f))
    print("Amount of old loaves:", float(o))
    print("Total Amount:", f+o)
