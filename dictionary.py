s=input("enter a string:")
d={}
if s.isspace():
    print("string is empty")
elif s.isdigit():
    print("enter characters only")
else:
    for i in s:
        d[i]=s.count(i)
    print(d)
