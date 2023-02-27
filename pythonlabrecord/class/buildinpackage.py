class publisher:

    name=''

    def __init__(self,n):
        self.name=n

    def display(self):
        print("the publisher is",self.name)

class book(publisher):
    title=""
    other=""
    def __init__(self,t,a):
        self.title=t
        self.other=a
        super().__init__(n)
    def display(self):
        super().display()
        print("auther=",self.other)
        print("titlte",self.title)

class python(book):

    prise=0
    num=0

    def __init__(self,t,a,n,p,no):
        self.prise=p
        self.num=no
        super().__init__(a,t)

    def display(self):
        super().display()
        print("the prze",self.prise)
        print("number of pages",self.num)

h=python("spire","ashwin","dc",250,432)
h.display()



