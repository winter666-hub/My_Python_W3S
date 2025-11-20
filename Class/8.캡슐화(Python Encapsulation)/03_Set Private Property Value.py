class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("나이는 양수여야 합니다.")

p1 = Person("겨우리", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())