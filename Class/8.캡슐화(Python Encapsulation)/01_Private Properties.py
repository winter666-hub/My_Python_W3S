class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # 클래스 내부의 데이터 보호

p1 = Person("겨우리", 25)
print(p1.name)
print(p1.age)