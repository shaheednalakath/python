choice=int(input("1 for find area Square 2 for rectangle 3 for triangle"))
if choice==1:
    a=int(input("enter the side"))
    sqr=lambda a:a*a
    print("area",sqr(a))
elif choice==2:
    l = int(input("enter the length"))
    b = int(input("enter the breadth"))
    rec = lambda l, b: l * b
    print(rec(l, b))
elif choice==3:
    b = int(input("enter the breadth"))
    h = int(input("enter the height"))
    tri=lambda b,h : 1/2*(b*h)
    print("area=",tri(b,h))
else:
    print("invalid choice")