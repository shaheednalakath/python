limit=int(input("enter the limit"))
count=0
n1,n2=0,1
if limit<=0:
    print("enter a positive integer")
elif limit==1:
    print(n1)
else:
    for i in  range(0,limit):
        print(n1)
        fibo=n1+n2
        n1=n2
        n2=fibo

# enter the limit5
# 0
# 1
# 1
# 2
# 3