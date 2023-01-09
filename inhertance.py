class a:
    def method(self):
        print("parent class")
        return ("123#2123iututmytn")
class b(a):
    def method_b(self):
        print("child classs b")
        return ("@#24htru43348w")
class c(b):
    def method_c(self):
        print("final class")
        return ("rewyw hsgdfhh@313yu5uui2yuiki094")


obj_c=c()
print(obj_c.method(),obj_c.method_b(),obj_c.method_c())

