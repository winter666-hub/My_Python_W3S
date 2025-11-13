class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("겨우리", 25)

del p1.age

print(p1.name)
print(p1.age) # p1 객체에는 age 속성이 존재하지 않는다.
# AttributeError 발생
