class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def celebrate_birthday(self):
        self.age += 1
        print(f"생일 축하해! 넌 이제 {self.age}살이야!")
    
p1 = Person("겨우리", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()    