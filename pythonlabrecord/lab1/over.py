li=[]
start=int(input("enter"))
end=int(input("enter"))
for i in range(start,end+1):
    if i<=100:
        li.append(i)
    else:
        li.append("over")
        break
