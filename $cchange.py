strw=str(input ("enter a string"))
z=strw[0]
l=strw[-1]
li=[]
li=list(strw)
print(li)
li[0]=l;
li[-1]=z;
print(''.join(li))
