

sentences=input("enter a word").split()
counts=dict()
for i in sentences:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1
print(counts)



sentences=input("enter a word")
counts=dict()
print(sentences)
for i in sentences:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1
print(counts)
