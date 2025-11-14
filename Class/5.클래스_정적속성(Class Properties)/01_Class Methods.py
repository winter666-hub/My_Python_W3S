class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("안녕, 내 이름은 " + self.name)
        
p1 = Person("겨우리")
p1.greet()