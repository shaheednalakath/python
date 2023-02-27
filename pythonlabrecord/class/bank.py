# class bankaccount:
#
#     def __init__(self,accno,name,type,bal):
#         self.c_accno=accno
#         self.c_name=name
#         self.c_type=type
#         self.c_balance=bal
#
#     def deposit(self,amound):
#         self.c_balance=self.c_balance+amound
#         print(self.c_balance)
#
#     def withdraw(self,amound):
#         self.c_balance=self.c_balance-amound
#         print(self.c_balance)
#
#     def accdetails(self):
#         print(self.c_name)
#         print(self.c_type)
#         print(self.c_accno)
#         print(self.c_balance)
#
# bank=bankaccount(123,"shaheed","savings",30000)
# bank.deposit(200000)
# bank.accdetails()
# bank.withdraw(100000)

class bank:
    def __init__(self,name,accno,deposit):
        self.nameof_cus=name
        self.accno_cus=accno
        self.bal_cus=deposit
    def create_acc(self):
        print("acc created")
    def display(self):
        print(self.nameof_cus)
        print(self.accno_cus)
        print(self.bal_cus)
    def deposit(self,amound):
        self.bal_cus=self.bal_cus+amound
        return self.bal_cus
    def wit_release(self,amound):
        self.bal_cus=self.bal_cus-amound
        return self.bal_cus
objbank=bank("shaheed",12345,10000)
objbank.create_acc()
print(objbank.display())
n=True
while n:
    print("1-depo")
    print("2-wi")
    print("3 exit")
    c=int(input("enter ch"))
    if c==1:
        n=int(input("enter amount to add"))
        objbank.deposit(n)
        objbank.display()
    elif c==2:
        n=int(input("enter amount to relase"))
        if n<objbank.bal_cus:
           objbank.wit_release(n)
           objbank.display()
        else:
            print("witdraw not possible")
    elif c==3:
        n=False
