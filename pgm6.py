n=int(input("how many names do you want to add"))
a=[]
print("enter names")
for i in range(0,n):
    name=input("")
    a.append(name)
print(a)
count=0
for i in a:
        count+= i.count("a")
print(count)

