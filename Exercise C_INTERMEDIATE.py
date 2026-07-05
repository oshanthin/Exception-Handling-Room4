num = 10
try:
    num.append(5)   
except AttributeError as e:
    print("Case 1 triggered AttributeError:", e)



class Student:
    def __init__(self):
        self.name = "Oshanthi"

s = Student()

try:
    print(s.age)   
except AttributeError as e:
    print("Case 2 triggered AttributeError:", e)

