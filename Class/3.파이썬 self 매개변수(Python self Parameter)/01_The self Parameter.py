class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("안녕하세요 저의 이름은 " + self.name)

p1 = Person("Winter", 25)
p1.greet()