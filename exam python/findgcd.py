def gcd(x,y):
    while (y):
        x,y=y,x%y
    return (x)
x=int(input("ent a"))
y=int(input("enter b"))
print(gcd(x,y));
