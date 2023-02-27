l=[]
li=[]
start=int(input("enter range"));
end=int(input("enter range"));
for i in range(start,end):
  if i>0:
     l.append(i)
print(l)
for i in l:
    print(i**2)

# word=str(input("enter a word"))
# vo=['a','e','i','o','u']
# for i in word:
#     if i.lower() in vo:
#         li.append(i)
# print(list(set(li)))
# w=[]
l=[]
word=input(("enter a word"))
voewls=('a','e','i','o','u')
for i in word:
    if i.lower() in voewls:
        l.append(i)
print(set(list(l)))

w=[]
word=input("enter a word")
for i in word:
    w.append(ord(i))
print(list(set(w)))    
    

