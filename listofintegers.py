a=[]
b=[]
n1=int(input("How many elements do you want in the first list"))
print("enter the values")
for i in range(0,n1):
    m=int(input(""))
    a.append(m)
print("the first list is",a)
n2=int(input("How many elements do you want in the second list"))
print("enter the values")
for i in range(0,n2):
    z=int(input(""))
    b.append(z)
print("the seccond list is",b)
if len(a)==len(b):
    print("they are of the same length")
else:
    print("they are of different lengths")
sum1=0;
sum2=0;
for x in a:
    sum1=sum1+x
print("the sum of first list is",sum1)

for x in b:
    sum2=sum2+x
print("the sum of second list is",sum2)

if sum1==sum2:
    print("the sum of both the lists are equal")
else:
    print("the sum of both the lists are not equal")
print("the common values are")
for num in a:
    if num in b:
        print(num)
    else:
        print("none")
        break