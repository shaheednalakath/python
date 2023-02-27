l=[]
m=[]
n=3
for i in range(n):
    ch=str(input("enter list elements"))
    l.append(ch)
for i in range(n):
    ch=str(input("enter list elements"))
    m.append(ch)
list1=set(l)
list2=set(m)
print(list1.difference(list2))
