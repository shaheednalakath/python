l=[]
sum=0
size=int(input("enter size of list"))
for i in range(size):
    l_items=int(input("enter numbers"))
    l.append(l_items)
print(l)
for i in l:
    sum=sum+i
print(sum)    