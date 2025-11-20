class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("Hello!")

p1 = Person("겨우리")

del Person.greet

p1.greet()