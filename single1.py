class parent():
    def __init__(self,a):
        self.a=a
    def fun1(self):
        print("A:",self.a)
class child(parent):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def fun2(self):
        print("B:",self.b)
c=child(5,6)
c.fun1()
c.fun2()
