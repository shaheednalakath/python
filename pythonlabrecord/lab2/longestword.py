# def findoflongestword(l):
#     n=max(l)
#     print("n=",n)
#     count=0
#     for i in n:
#         count+=1
#     print(count)
# n=int(input("enter number of words"))
# l=[]
# for i in range(n):
#     str=input("enter word")
#     l.append(str)
# findoflongestword(l)
#
def findlongestword(list_lis):
    n=max(list_lis)
    count=0
    for i in n:
        if i != ' ':
            count+=1
    print(count)
l=[]
n=int(input("enter number of word in list"))
for i in range(n):
    st=input("enter data")
    l.append(st)
findlongestword(l)

