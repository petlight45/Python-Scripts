def average(list_obj):
    pass

class Student:
    def __init__(self,age, weight, height):
        global list_std_obj
        self.age = age
        self.weight = weight
        self.height = height
        list_std_obj.append(self)
    def info(self):
        return round(self.weight/(self.height**2), 2)

list_std_obj = []
Student(12,3,2)
Student(12,3,2)
print(list_std_obj)
print(list_std_obj[-1].age)
