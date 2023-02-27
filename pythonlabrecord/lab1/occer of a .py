word=input("enter  a string")
count=dict()
for i in word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count['a'])

