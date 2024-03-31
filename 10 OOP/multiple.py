   
class Add:
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
        
    def add(self):
        return self.no1+self.no2

class Sub:
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
       
    def sub(self):
        return self.no1-self.no2
    
class Aithmetic(Add,Sub):
    def __init__(self, no1, no2):
        super().__init__(no1, no2)
    
    
    
a=Aithmetic(12,89)
print(a.add())
print(a.sub())