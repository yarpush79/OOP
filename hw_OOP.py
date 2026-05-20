class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)

        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)

        if all_grades:
            avg = sum(all_grades) / len(all_grades)
        else:
            avg = 0

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg:.1f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._average_grade() <= other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._average_grade() >= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._average_grade() == other._average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._average_grade() != other._average_grade()

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)

        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)

        if all_grades:
            avg = sum(all_grades) / len(all_grades)
        else:
            avg = 0

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg:.1f}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._average_grade() <= other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._average_grade() >= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._average_grade() == other._average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._average_grade() != other._average_grade()


class Reviewer(Mentor):
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        
def average_hw_grade_by_course(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            for grade in student.grades[course]:
                all_grades.append(grade)

    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0

def average_lecture_grade_by_course(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            for grade in lecturer.grades[course]:
                all_grades.append(grade)

    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0

# Проверка по заданию 1

print()
print("---Проверка по заданию 1---")
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

# Проверка по заданию 2

print()
print("---Проверка по заданию 2---")
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
print(lecturer.grades)  # {'Python': [7]}  

# Проверка по заданию 3

print()
print("---Проверка по заданию 3---")

some_student = Student("Ruoy", "Eman", "м")
some_student.courses_in_progress += ["Python", "Git"]
some_student.finished_courses += ["Введение в программирование"]

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ["Python"]

some_reviewer = Reviewer("Some", "Buddy")
some_reviewer.courses_attached += ["Python"]

some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 9)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)
some_reviewer.rate_hw(some_student, "Python", 10)

some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 10)
some_student.rate_lecture(some_lecturer, "Python", 9)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)

# Проверка сравнения

print()
print("--- Сравнение студентов ---")
some_reviewer.rate_hw(student, "Python", 8)
some_reviewer.rate_hw(student, "Python", 7)

print(student)
print(some_student)
print(some_student > student)   # True  
print(some_student < student)   # False
print(some_student == student)  # False
print(some_student != student)  # True

print()
print("--- Сравнение лекторов ---")
some_student.rate_lecture(lecturer, "Python", 8)
some_student.rate_lecture(lecturer, "Python", 9)

print(lecturer)
print(some_lecturer)
print(some_lecturer > lecturer)   # True  
print(some_lecturer >= lecturer)  # True
print(some_lecturer < lecturer)   # False
print(some_lecturer == lecturer)  # False

print()
print("--- Попытка сравнить разные типы ---")
print(some_student > some_lecturer)   # Ошибка

# Проверка по заданию 4

print()
print("---Проверка по заданию 4---")

# --- Создаём по 2 экземпляра каждого класса ---

# Студенты
student_1 = Student("Ruoy", "Eman", "м")
student_1.courses_in_progress += ["Python", "Git"]
student_1.finished_courses += ["Введение в программирование"]

student_2 = Student("Анна", "Смирнова", "ж")
student_2.courses_in_progress += ["Python", "Git"]
student_2.finished_courses += ["Введение в программирование"]

# Лекторы
lecturer_1 = Lecturer("Иван", "Иванов")
lecturer_1.courses_attached += ["Python"]

lecturer_2 = Lecturer("Пётр", "Петров")
lecturer_2.courses_attached += ["Python", "Git"]

# Ревьюеры
reviewer_1 = Reviewer("Some", "Buddy")
reviewer_1.courses_attached += ["Python"]

reviewer_2 = Reviewer("Other", "Reviewer")
reviewer_2.courses_attached += ["Python", "Git"]

# --- Вызываем rate_hw (Reviewer ставит оценки студентам) ---

reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_1, "Python", 10)
reviewer_2.rate_hw(student_1, "Git", 8)

reviewer_1.rate_hw(student_2, "Python", 7)
reviewer_2.rate_hw(student_2, "Python", 8)
reviewer_2.rate_hw(student_2, "Git", 9)

# --- Вызываем rate_lecture (Student оценивает лекторов) ---

student_1.rate_lecture(lecturer_1, "Python", 10)
student_1.rate_lecture(lecturer_1, "Python", 9)
student_1.rate_lecture(lecturer_2, "Python", 8)
student_1.rate_lecture(lecturer_2, "Git", 10)

student_2.rate_lecture(lecturer_1, "Python", 7)
student_2.rate_lecture(lecturer_2, "Python", 9)
student_2.rate_lecture(lecturer_2, "Git", 8)

# --- Печать через __str__ ---

print("--- Студенты ---")
print(student_1)
print()
print(student_2)

print()
print("--- Лекторы ---")
print(lecturer_1)
print()
print(lecturer_2)

print()
print("--- Ревьюеры ---")
print(reviewer_1)
print()
print(reviewer_2)

# --- Сравнения ---

print()
print("--- Сравнение студентов ---")
print(f"{student_1.name} > {student_2.name}: {student_1 > student_2}")
print(f"{student_1.name} == {student_2.name}: {student_1 == student_2}")

print()
print("--- Сравнение лекторов ---")
print(f"{lecturer_1.name} > {lecturer_2.name}: {lecturer_1 > lecturer_2}")
print(f"{lecturer_1.name} < {lecturer_2.name}: {lecturer_1 < lecturer_2}")

# --- Средние по курсу ---

print()
print("--- Средние оценки по курсам ---")

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

avg_hw_python = average_hw_grade_by_course(students, "Python")
avg_hw_git = average_hw_grade_by_course(students, "Git")
print(f"Средняя оценка за ДЗ по курсу Python: {avg_hw_python}")
print(f"Средняя оценка за ДЗ по курсу Git: {avg_hw_git}")

avg_lect_python = average_lecture_grade_by_course(lecturers, "Python")
avg_lect_git = average_lecture_grade_by_course(lecturers, "Git")
print(f"Средняя оценка за лекции по курсу Python: {avg_lect_python}")
print(f"Средняя оценка за лекции по курсу Git: {avg_lect_git}")