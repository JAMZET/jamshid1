class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} жүйеге кірді")

class Student(User):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        self.courses.append(course)
        print(f"{self.name} {course.name} курсына тіркелді")

class Teacher(User):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def give_grade(self, student, grade):
        print(f"{student.name} бағасы: {grade}")

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class University:
    def __init__(self, name):
        self.name = name
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.teachers = []

class Exam:
    def __init__(self, course):
        self.course = course

    def take_exam(self, student, grade):
        print(f"{student.name} емтиханнан {grade} алды")

uni = University("SDU")

student = Student("Жамшид", 123)
teacher = Teacher("Асан")

course = Course("Python")

student.login()
student.register_course(course)

teacher.add_course(course)
teacher.give_grade(student, 95)

exam = Exam(course)
exam.take_exam(student, 90)
