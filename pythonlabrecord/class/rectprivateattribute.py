# class rectangle:
#
#     def __init__(self,len,ber):
#         self.l=len
#         self.b=ber
#
#     def area(self):
#         return (self.l*self.b)
#
#     def __lt__(self, other):
#         if self.area()<other.area():
#             return print("a1 is ls")
#         else:
#             return print("a2 is grather")
# obj1=rectangle(2,3)
# obj2=rectangle(3,2)
# print("print area 1",obj1.area())
# print("print area 2",obj2.area())
# obj1<obj2
#
# class rect:
#     __len=0
#     __wid=0
#     def __init__(self,len,ber):
#         self.__len=len
#         self.__wid=ber
#
#
#     def area(self):
#         return self.__wid*self.__len
#
#     def __lt__(self, other):
#         if self.area()<other.area():
#             print("a2 is larger")
#         else:
#             print("a1 is larger")
#
# obj1=rect(3,2)
# obj2=rect(2,3)
# obj1<obj2
class rect:
    __len=0
    __ber=0
    def __init__(self,l,b):
        self.__len=l
        self.__ber=b
    def area(self):
        return self.__ber*self.__len
    def __lt__(self, other):
        if(self.area()<other.area()):
            print("a2 is larg")
        else:
            print("a1 is larg")


obj1=rect(2,3)
obj2=rect(3,4)
obj1<obj2

