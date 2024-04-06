print('DZ30')


class GroupMaximumAmountError(Exception):
    def __init__(self, message="Group maximum amount error"):
        super().__init__()
        self.message = message


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"


class Group:
    maxStudents = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.maxStudents:
            raise GroupMaximumAmountError()
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        temp = self.find_student(last_name)
        if temp is not None:
            self.group.remove(temp)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Number:{self.number}\n{all_students} '


gr = Group('PD1')

try:
    for i in range(11):
        gr.add_student(Student('Male', 30, 'Steve', 'Jobs', 'AN142'))
except GroupMaximumAmountError as e:
    print(e.message)

print('Thank you for using')