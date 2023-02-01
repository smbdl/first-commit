class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = str(fullname).title()
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname}\nAge: {self.age}\nIs married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = dict(marks)

    def marks_average(self):
        print(f"{self.fullname}'s marks average: {sum(self.marks.values()) / len(self.marks.keys())}")


class Teachers(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def count_salary(self):
        if self.experience > 3:
            return f'{self.salary + (self.salary * 0.05) * (self.experience - 3)}'
        else:
            print(f'{self.salary}')


# teacher = Teachers('Marina', 30, 'yes', 5, 10000)
# teacher.introduce_myself()
# print(f'Experience: {teacher.experience} years\nSalary: {teacher.count_salary()} soms')

def create_student(name: str, marks: dict):
    average = sum(marks.values()) / len(marks.keys())
    students_list = [name.title(), marks, round(average, 2)]
    return students_list


print(create_student('Max', {'math': 5, "biology": 4, "p.e": 5}))
