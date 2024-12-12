class Mentor:
    def __init__(self, name, surname, courses):
        self.name = name
        self.surname = surname
        self.courses = courses


class Reviewer(Mentor):
    def __init__(self, name, surname, courses):
        super().__init__(name, surname, courses)
        self.reviews = []

    def give_review(self, student, grades):
        """Рецензент выставляет оценку студенту"""
        for grade in grades:  
            student.receive_grade(self, grade) 
        self.reviews.append((student.name, grades))

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


class Lecturer(Mentor):
    def __init__(self, name, surname, courses):
        super().__init__(name, surname, courses)
        self.lec_reviews = []

    def receive_grades(self, student, grades):
        """Преподаватель получает оценки от студентов"""
        if student.courses in self.courses:  
            self.lec_reviews.append((student.name, grades))  
        else:
            print(f'Оценки по курсу {student.courses} отсутствуют')

    def average_grade(self):
        """Функция для вычисления среднего значения"""
        all_grades = []
        for _, grades in self.lec_reviews:
            all_grades.append(grades)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def __add__(self, lecturer):
        return f"{self.name} имеет оценку ({self.average_grade():.2f}), а {lecturer.name} имеет оценку ({lecturer.average_grade():.2f})\n"

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка лекции: {self.average_grade():.2f}\n')


class Student:
    def __init__(self, name, surname, courses):
        self.name = name
        self.surname = surname
        self.courses = courses
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def receive_grade(self, reviewer, grade):
        """Студент получает оценку от рецензента"""
        if self.courses not in self.grades:
            self.grades[self.courses] = []
        self.grades[self.courses].append((reviewer.name, grade)) 

    def give_grades_to_lecturer(self, lecturer, grades):
        """Студент оценивает преподавателя"""
        if self.courses in lecturer.courses:  
            for grade in grades:  
                lecturer.receive_grades(self, grade)  
        else:
            print("Оценки отсутствуют")

    def average_grade(self):
        """Функция для вычисления среднего значения"""
        all_grades = []
        for course_grades in self.grades.values():
            for _, grade in course_grades:
                all_grades.append(grade)
        if not all_grades:  
            return 0
        return sum(all_grades) / len(all_grades)
                
    def __add__(self, student):
        return f"{self.name} имеет оценку ({self.average_grade():.2f}), а {student.name} имеет оценку ({student.average_grade():.2f})\n"

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.2f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')


def average_grade_students(students, course):
    """Функция для вычисления средней оценки за домашние задания по всем студентам в рамках конкретного курса"""
    all_grades = []
    for student in students:
        if course in student.grades:
            for _, grade in student.grades[course]:
                all_grades.append(grade)
    if not all_grades:  # Проверка на случай, если оценок нет
        return 0
    return sum(all_grades) / len(all_grades)

def average_grade_lecturers(lecturers, course):
    """Функция для вычисления средней оценки за лекции всех лекторов в рамках курса"""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.courses:
            for _, course_grades in lecturer.lec_reviews:
                all_grades.append(course_grades)
    if not all_grades:  # Проверка на случай, если оценок нет
        return 0
    return sum(all_grades) / len(all_grades)                
    


reviewer2 = Reviewer("Андрей", "Петров", "Git ")
reviewer1 = Reviewer("Геннадий", "Осипов", "Python ")

student1 = Student("Владимир", "Иванов", "Python")
student1.finished_courses = ["Git"]
student1.courses_in_progress = ["Python", "Quality Control Specialist"]

student2 = Student("Иван", "Кузьмин", "Git")
student2.finished_courses = ["Java", "BI"]
student2.courses_in_progress = ["Python", "Git"]

student3 = Student("Магомет", "Ибрагимов", "Git")
student3.finished_courses = ["Java", "BI"]
student3.courses_in_progress = ["Python", "Git"]

student4 = Student("Даниил", "Иванов", "Python")
student4.finished_courses = ["Git"]
student4.courses_in_progress = ["Python", "Quality Control Specialist"]



lecturer1 = Lecturer("Дмитрий", "Ветров", "Python")
lecturer2 = Lecturer("Анатолий", "Муромов", "Git")
lecturer3 = Lecturer("Егор", "Медваедев", "Python")
lecturer4 = Lecturer("Мануфий", "Абрамов", "Git")

reviewer1.give_review(student1, [5, 9, 10, 6, 5])
reviewer2.give_review(student2, [4, 3, 9, 10])
reviewer1.give_review(student3, [7, 10, 10, 8, 6])
reviewer2.give_review(student4, [7, 5, 6, 6, 4, 10])

student1.give_grades_to_lecturer(lecturer1, [8, 5, 5, 9])
student2.give_grades_to_lecturer(lecturer2, [7, 9, 6, 7])
student4.give_grades_to_lecturer(lecturer3, [10, 8, 7, 7, 9])
student3.give_grades_to_lecturer(lecturer4, [9, 7, 7, 10, 7])

print("Рецензенты:\n")
print(reviewer1)
print(reviewer2)

print("Студенты:\n")
print(student1)
print(student2)
print(student3)
print(student4)
print(student1.__add__(student3))
print(student4.__add__(student2))

print("Лекторы:\n")
print(lecturer1)
print(lecturer2)
print(lecturer3)
print(lecturer4)
print(lecturer3.__add__(lecturer2))
print(lecturer4.__add__(lecturer1))

print(f'Средняя оценка за домашние задания по курсу "Python": {average_grade_students([student1, student3], "Python"):.2f}')
print(f'Средняя оценка за домашние задания по курсу "Git": {average_grade_students([student2, student4], "Git"):.2f}')


print(f'Средняя оценка за лекции курса "Python": {average_grade_lecturers([lecturer1, lecturer3], "Python"):.2f}')
print(f'Средняя оценка за лекции курса "Git": {average_grade_lecturers([lecturer2, lecturer4], "Git"):.2f}')
