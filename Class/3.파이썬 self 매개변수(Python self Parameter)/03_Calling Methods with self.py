class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return "안녕, " + self.name
    
    def welcome(self):
        message = self.greet()
        print(message + "! 웹 사이트에 온 걸 환영해!")

p1 = Person("겨우리")
p1.welcome()