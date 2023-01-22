str=(input("enter a data"))
if str[-3:]=='ing':
    str+="ly"
else:
    str+="ing"
print(str)