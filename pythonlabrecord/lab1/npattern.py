n=1
def sum(n):
    sum=0
    sum=((n)+(n*10+n)+(n*100+n*10+n))
    print(sum)
i=1

while(i<=3):
    j=1
    while(j<=i):
        print(1,end="")
        j=j+1
    print(end="+")
    i=i+1
print()
sum(n)
