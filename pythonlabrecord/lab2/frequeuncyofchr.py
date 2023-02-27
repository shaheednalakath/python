# str=input("enter s string")
# count=dict()
# for i in str:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)
str=input("enter str")
count=dict()
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count['s'])