class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age # return문

p1 = Person("겨우리", 25)
print(p1.get_age()) # get 메소드로 호출