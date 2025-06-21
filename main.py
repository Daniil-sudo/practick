class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, course, grade, lecturer):
        if not isinstance(grade, (int, float)):
            return 'Ошибка: оценка должна быть числом'
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: оценивать можно только лекторов'
        if course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка: лектор не ведет этот курс'

    def rate_hw(self, course, grade, reviewer):
         if not isinstance(grade, (int, float)):
            return 'Ошибка: оценка должна быть числом'
         if not isinstance(reviewer, Reviewer):
            return 'Ошибка: ДЗ может проверять только ревьювер'
         if course in reviewer.courses_attached and course in self.courses_in_progress:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
         else:
            return 'Ошибка: ревьювер не ведет этот курс, или студент не записан на этот курс'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.get_avg_grade()}\n" \
               f"Курсы в процессе изучения: {courses_in_progress_string}\n" \
               f"Завершенные курсы: {finished_courses_string}"

    def get_avg_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return sum(grades_list) / len(grades_list)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка: сравнение возможно только между студентами'
        return self.get_avg_grade() < other.get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка: сравнение возможно только между студентами'
        return self.get_avg_grade() <= other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка: сравнение возможно только между студентами'
        return self.get_avg_grade() == other.get_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка: сравнение возможно только между студентами'
        return self.get_avg_grade() != other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка: сравнение возможно только между студентами'
        return self.get_avg_grade() > other.get_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка: сравнение возможно только между студентами'
        return self.get_avg_grade() >= other.get_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Инициализируем grades пустым словарем

    def __str__(self):
        grades_list = []
        if self.grades:
            for grade in self.grades.values():
                grades_list.extend(grade)
            avg_grade = sum(grades_list) / len(grades_list)
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"
        else:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nОценок за лекции пока нет"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка: сравнение возможно только между лекторами'
        if not self.grades:
            return False
        if not other.grades:
            return True

        avg_grade_self = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) if self.grades else 0
        avg_grade_other = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])) if other.grades else 0
        return avg_grade_self < avg_grade_other

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка: сравнение возможно только между лекторами'
        if not self.grades:
            return False
        if not other.grades:
            return True

        avg_grade_self = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) if self.grades else 0
        avg_grade_other = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])) if other.grades else 0
        return avg_grade_self <= avg_grade_other

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка: сравнение возможно только между лекторами'
        if not self.grades and not other.grades:
            return True
        if not self.grades or not other.grades:
            return False

        avg_grade_self = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) if self.grades else 0
        avg_grade_other = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])) if other.grades else 0
        return avg_grade_self == avg_grade_other

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка: сравнение возможно только между лекторами'
        if not self.grades and not other.grades:
            return False
        if not self.grades or not other.grades:
            return True
        avg_grade_self = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) if self.grades else 0
        avg_grade_other = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])) if other.grades else 0
        return avg_grade_self != avg_grade_other

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка: сравнение возможно только между лекторами'
        if not self.grades:
            return True
        if not other.grades:
            return False
        avg_grade_self = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) if self.grades else 0
        avg_grade_other = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])) if other.grades else 0
        return avg_grade_self > avg_grade_other

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка: сравнение возможно только между лекторами'
        if not self.grades:
            return True
        if not other.grades:
            return False

        avg_grade_self = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) if self.grades else 0
        avg_grade_other = sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])) if other.grades else 0
        return avg_grade_self >= avg_grade_other


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
         if not isinstance(grade, (int, float)):
            return 'Ошибка: оценка должна быть числом'
         if not isinstance(student, Student):
             return 'Ошибка: Проверять можно только студентов'
         if course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
         else:
            return 'Ошибка: ревьювер не ведет этот курс, или студент не записан на этот курс'


# Функции для подсчета средних оценок
def calculate_avg_hw_grade_for_course(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    if count == 0:
        return 0
    return total_grade / count


def calculate_avg_lecture_grade_for_course(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count == 0:
        return 0
    return total_grade / count


# Создание экземпляров классов
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')
reviewer1 = Reviewer('Сергей', 'Сергеев')
reviewer2 = Reviewer('Ольга', 'Ольгина')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Сидоров', 'Иван', 'М')

# Назначение курсов
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'Git', 'C++']
student2.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python']
reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['C++']

# Проверка выставления оценок лектору
student1.rate_lecture('Python', 7, lecturer1)
student1.rate_lecture('Python', 9, lecturer1)
student2.rate_lecture('Python', 8, lecturer1)
student1.rate_lecture('C++', 8, lecturer1)

student1.rate_lecture('Python', 10, lecturer2)

# Проверка выставления оценок студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student2, 'C++', 9)
student2.rate_hw('C++', 10, reviewer2) # Ошибка, ДЗ может проверять только ревьювер.

#  добавлена проверка на ввод для ревьювера и студента

# Проверка сравнения лекторов
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 == lecturer2)

# Проверка сравнения студентов
print(student1 > student2)
print(student1 < student2)
print(student1 == student2)

# Вывод информации об экземплярах классов
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
print(student1)
print(student2)

# Вызов функций для подсчета средних оценок
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу Python: {calculate_avg_hw_grade_for_course(students_list, 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {calculate_avg_lecture_grade_for_course(lecturers_list, 'Python')}")
print(f"Средняя оценка за домашние задания по курсу Git: {calculate_avg_hw_grade_for_course(students_list, 'Git')}")
print(f"Средняя оценка за лекции по курсу С++: {calculate_avg_lecture_grade_for_course(lecturers_list, 'C++')}")