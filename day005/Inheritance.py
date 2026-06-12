#INHERITANCE
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class dog(Animal):
    def speak(self):
        return f"{self.name} sayes woof!" 

class cat(Animal):
    def speak(self):
        return f"{self.name} sayes Meow!" 

d=dog("muko")
c=cat("michan")

print(d.speak())
print(c.speak())
print(type(d))
print(isinstance(d,Animal))# it checks whether d belongs to the class Animal
