class Student:

    def __init__(self, name, surname, gender):

        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, course, grade, lecturer):
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
            return lecturer.grades

class Mentor:

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = None

    def __str__(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {sum(grades_list) / len(grades_list)}")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):

        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]

        def __str__(self):
            return f"Имя: {self.name} \nФамилия: {self.surname}"


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture('Python', 7))  # None
print(student.rate_lecture('Java', 8))  # Ошибка
print(student.rate_lecture('С++', 8))  # Ошибка
print(student.rate_lecture('Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}  