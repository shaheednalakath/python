year=int(input("enter a year"))
fut=int(input("enter a year"))
if year>fut:
    print("fut year mut to be grater than current year")
else:
    for i in range(year,fut+1):
        if(i%4==0 and i%400 !=0 or i%100==0):
            print(i)
        
