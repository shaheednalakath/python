def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2);



x=int(input("enter a fnumber"))
for i in range(0,x+1):
    print(fib(i))