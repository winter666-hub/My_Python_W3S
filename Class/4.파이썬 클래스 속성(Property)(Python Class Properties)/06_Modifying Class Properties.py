class Person:
    lastname = ""
    
    def __init__(self, name):
        self.name = name

p1 = Person("겨우리")
p2 = Person("에밀리")

Person.lastname = "나무"

print(p1.lastname)
print(p2.lastname)