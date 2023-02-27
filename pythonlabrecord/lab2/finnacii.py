def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=5
for i in range(n):
    print(fib(i))
m=5
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(m))
