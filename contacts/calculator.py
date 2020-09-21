class Calculator:
    def __init__(self, num1, num2):  # self는 외부에서 작성하는 키워드
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

                                                                                                                                                                                                                  
if __name__ == "__main__":
    calc = Calculator(6, 2)  # num1 = 6, num2 = 2
    sumResult = calc.sum()
    subResult = calc.sub()
    multResult = calc.mult()
    divResult = calc.div()

    print('덧셈결과 {}'.format(sumResult))
    print('뺄셈결과 {}'.format(subResult))
    print('곱셈결과 {}'.format(multResult))
    print('나눗셈결과 {}'.format(divResult))

    # 덧셈결과 : 8
    # 뺄셈결과 : 4
    # 곱셈결과 : 12
    # 나눗셈결과 : 3
