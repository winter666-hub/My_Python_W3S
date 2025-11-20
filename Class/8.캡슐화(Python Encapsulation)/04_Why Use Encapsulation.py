class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0
    
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("나이는 0부터 100이어야 합니다.")
        
    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
        
student = Student("겨우리")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())