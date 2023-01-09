len=int(input("How many numbers you want to store"))
list=[]
print("enter the values")
for i in range(0,len):
    x=int(input(""))
    if x>100:
        list.append("over")
    else:
        list.append(x)
print(list)