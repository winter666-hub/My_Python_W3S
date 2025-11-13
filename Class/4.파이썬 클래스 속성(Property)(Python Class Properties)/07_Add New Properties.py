class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("겨우리")

p1.age = 25 # __init__에서 정의하지 않아도 속성을 추가할 수 있다.
p1.city = "서울" # 파이썬은 객체에 새로운 속성을 자유롭게 추가할 수 있다.

print(p1.name)
print(p1.age)
print(p1.city)