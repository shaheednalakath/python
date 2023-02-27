# class name:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=name("sam",65)
# print(p1.name)
# print(p1.age)
# class rectangle:
#
#     def __init__(self,len,ber):
#         self.l=len
#         self.b=ber
#
#     def area(self):
#         return (self.l*self.b)
#     def per(self):
#         return (2*self.l+2*self.b)
#     def __lt__(self, other):
#         if self.area()<other.area():
#             return print("a1 is ls")
#         else:
#             return print("a2 is grather")
# obj1=rectangle(2,3)
# obj2=rectangle(3,2)
# print("print area 1",obj1.area())
# print("print area 2",obj2.area())
# print(obj1.per())
# print(obj2.per())
# obj1<obj2
class rectangle:

    def __init__(self,l,b):
        self.len=l
        self.ber=b
    def area(self):
        return self.len*self.ber
    def perimeter(self):
        return 2*self.ber*2*self.bar
    def __lt__(self, other):
        if(self.area()<other.area()):
            print("a2")
        else:
            print("a1")
obj1=rectangle(2,3)
obj2=rectangle(4,2)
obj1<obj2