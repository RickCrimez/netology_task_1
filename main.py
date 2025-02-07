class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0

    def __str__(self):
        avg = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет завершенных курсов'
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Студентов можно сравнивать только со студентами!'
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Студентов можно сравнивать только со студентами!'
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Студентов можно сравнивать только со студентами!'
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0

    def __str__(self):
        avg = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лекторов можно сравнивать только с лекторами!'
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лекторов можно сравнивать только с лекторами!'
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лекторов можно сравнивать только с лекторами!'
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


# Расчет средних значений оценок для студентов
def average_hw_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count != 0 else 0

# Расчет средних значений оценок для лекторов
def average_lecture_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count != 0 else 0


# Экземпляры классов Student, Lecturer, Reviewer
student1 = Student('Виктория', 'Калмыкова', 'female')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Анастасия', 'Сметанкина', 'female')
student2.courses_in_progress += ['Python', 'Git']

lecturer1 = Lecturer('Кирил', 'Касаткин')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Олег', 'Булыгин')
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('Никита', 'Чернецкий')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Артем', 'Дубовской')
reviewer2.courses_attached += ['Git']

# Оценки для студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'Git', 7)
reviewer2.rate_hw(student2, 'Git', 9)

# Оценки для лекторов
student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Git', 6)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Git', 10)


students = [student1, student2]
lecturers = [lecturer1, lecturer2]
reviewers = [reviewer1, reviewer2]
for student in students:
    print(student)
    print('-' * 50)

for lecturer in lecturers:
    print(lecturer)
    print('-' * 50)

for reviewer in reviewers:
    print(reviewer)
    print('-' * 50)


# Расчет средних оценок
print(f'Средняя оценка студентов по курсу: {average_hw_grade([student1, student2], 'Python')}')
print(f'Средняя оценка лекторов по курсу: {average_lecture_grade([lecturer1, lecturer2], 'Python')}')
print()

# Сравнение между студентами
if student1 > student2:
    print(f"{student1.name} лучше чем {student2.name} ")
elif student1 < student2:
    print(f"{student2.name} лучше чем {student1.name} ")
else:
    print("Студенты равны в своих оценках")

# Сравнение между лекторами
if lecturer1 > lecturer2:
    print(f"{lecturer1.name} преподаёт лучше чем {lecturer2.name} ")
elif lecturer1 < lecturer2:
    print(f"{lecturer2.name} преподаёт лучше чем {lecturer1.name} ")
else:
    print("Лекторы равны в своих оценках")

# Проверка недопустимого сравнения между объектами разных классов
print(lecturer1 > student1)
print(student2 < lecturer2)