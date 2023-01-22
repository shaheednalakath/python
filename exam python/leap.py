from datetime import datetime
year=datetime.today().year;
futy=int(input("enter cut year"))
if(year>futy):
     print("error");
else:
    for i in range(year,futy+1):
        if i%4 == 0 and i%400 == 0 or i%100 ==0:
            print(i);
