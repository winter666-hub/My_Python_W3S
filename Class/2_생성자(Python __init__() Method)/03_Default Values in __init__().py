class Person:
    def __init__(self, name, age = 20):
        self.name = name
        self.age = age
        
p1 = Person("Winter")
p2 = Person("Tree", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)