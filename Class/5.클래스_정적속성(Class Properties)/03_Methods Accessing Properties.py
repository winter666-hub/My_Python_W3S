class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_info(self):
        return f"{self.name}는 {self.age}살 입니다."

p1 = Person("겨우리", 25)
print(p1.get_info())
