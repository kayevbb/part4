class Student:
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.departament = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        Vasy = self.name + ' ' + self.last_name + ' Поступил ' + self.departament + ' ' + self.year_of_entrance
        return Vasy


student1 = Student("Вася", " Иванова", "  на факультеть програмирования", " в 2017г")

print(student1.get_student_info())