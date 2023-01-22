str=str(input("enter str"))
p={}
for i in str:
    if i in p:
        p[i]+=1
    else:
        p[i]=1
print(p)