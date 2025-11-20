class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("갸우리", 25)
print(p1._Person__age) # 캡슐화 목적 어긋남