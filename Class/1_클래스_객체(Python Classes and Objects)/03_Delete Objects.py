class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("안녕하세요 저의 이름은 " + self.name)
    
p1 = Person("winter666", 25)

del p1

print(p1)