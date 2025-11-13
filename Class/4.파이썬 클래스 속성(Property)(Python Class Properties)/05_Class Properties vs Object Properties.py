class Person:
    species = "사람" # 클래스 변수 (클래스 전체에서 사용하는 변수)
    
    def __init__(self, name):
        self.name = name # 인스턴스 변수 (각 인스턴스마다 다르다.)
    
p1 = Person("에밀리")
p2 = Person("겨우리")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)