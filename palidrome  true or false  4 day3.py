str=input("enter the number:")
str=str.casefold()
rev_str = reversed(str)
if list(str) == list(rev_str):
   print(True)
else:
   print(False)
