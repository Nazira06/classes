
class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop
        self.height = 0
        self.sex = ''
    def __str__(self):
        return f"Name:{self.name} laptop :{self.laptop} пол:{self.sex}"

vasya = Student('Vasya','Acer')
vasya.height = 150
vasya.sex = 'male'
emir = Student('Emir', 'Lenovo')
emir.height = 180
emir.sex = 'male'
nazira = Student('Nazira', 'Dell')
nazira.height = 156
nazira.sex = 'famale'
print(vasya, emir, nazira)
