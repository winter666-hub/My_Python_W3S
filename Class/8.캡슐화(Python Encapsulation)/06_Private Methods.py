class Calculator:
    def __init__(self):
        self.result = 0 # result 0으로 초기화

    def __validate(self, num):
        if not isinstance(num, (int, float)): # 정수인지 실수인지 확인
            return False
        return True
    
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number") # 정수나 실수가 아닐 시

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)

