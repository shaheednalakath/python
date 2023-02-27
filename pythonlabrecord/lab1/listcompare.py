l=[1,2,3,4,5]
m=[1,2,3,4,5]
sm=[]
for i in l:
    for j in m:
        if(i==j):
            sm.append(i)
print("same values are",sm)
clr=input("enter colors seprated by comma")
clr=clr.split(",")
print(clr[0],clr[-1])