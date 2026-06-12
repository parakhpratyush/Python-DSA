class student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def introduction(self):
        return f"I am {self.name} and i am {self.age} yaers old"
    
    def study(self,subject):
        return f"i am {self.name} studying {subject}"
    
s1=student("Beta Testor",18)
print(s1.introduction())
print(s1.study("python"))

