class A:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name is"+self.name)

class B(A):
    def __init__(self, name, addr):
        super().__init__(name)
        self.addr=addr
    def display(self):
        print("Name is"+self.name+"\n Address:"+self.addr)
    
class C(B):
     def __init__(self, name, addr,city):
        super().__init__(name,addr)
        self.city=city
     def display(self):
        print("Name is"+self.name+"\n Address:"+self.addr+"\n City"+self.city)

c=C("abc","plot no23,hjgdekjwjf","Jaysingpur")
c.display()
