class calculator:
    class_value = "shared value"
    def __init__(self):
        self.result = 0

    def add(self, val):
        self.result += val
    def min(self, val):
        pass

class calculatorMore(calculator):
    def min(self, val):
        self.result -= val

a = calculator()
a.add(1)
print(a.result) # 1
a.add(2)
print(a.result) # 3
a.min(1)
print(a.result) # 3

b = calculatorMore()
b.min(1) # -1

if id(calculator.class_value) == id(a.class_value): 
    print("class value") # Member Value 는 공유되는 변수이다.
if id(calculatorMore.class_value) == id(b.class_value): 
    print("class value") # Member Value 는 공유되는 변수이다.
if id(a.class_value) == id(b.class_value): 
    print("class value") # Member Value 는 공유되는 변수이다.
