def gcd(x,y):
    while(y):
        x,y=y,x%y
        print(x)
        print(y)
    print(x)

n=int(input("enter a number"))
m=int(input("enter a number"))
gcd(n,m)
