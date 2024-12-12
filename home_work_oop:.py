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
        for _, course_grades in self.lec_reviews: 
            all_grades.append(course_grades)  
        if not all_grades:  
            return 0
        return sum(all_grades) / len(all_grades)
    
    def __add__(self, lecturer):
        return f"{lecturer1.name} имеет оценку ({lecturer1.average_grade():.2f}), а {lecturer2.name} имеет оценку ({lecturer2.average_grade():.2f})\n"

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
        return f"{student1.name} имеет оценку ({student1.average_grade():.2f}), а {student2.name} имеет оценку ({student2.average_grade():.2f})\n"

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.2f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')



reviewer2 = Reviewer("Андрей", "Петров", "Git ")
reviewer1 = Reviewer("Геннадий", "Осипов", "Python ")

student1 = Student("Владимир", "Иванов", "Python")
student1.finished_courses = ["Git"]
student1.courses_in_progress = ["Python", "Quality Control Specialist"]

student2 = Student("Иван", "Кузьмин", "Git")
student2.finished_courses = ["Java", "BI"]
student2.courses_in_progress = ["Python", "Git"]

lecturer1 = Lecturer("Дмитрий", "Ветров", "Python")
lecturer2 = Lecturer("Анатолий", "Муромов", "Git")

reviewer1.give_review(student1, [5, 9, 10, 6, 5])
reviewer2.give_review(student2, [4, 3, 9, 10])

student1.give_grades_to_lecturer(lecturer1, [8, 5, 5, 9])
student2.give_grades_to_lecturer(lecturer2, [7, 9, 6, 7])

print("Рецензенты:\n")
print(reviewer1)
print(reviewer2)
print("Студенты:\n")
print(student1)
print(student2)
print(student1.__add__(student2))
print("Лекторы:\n")
print(lecturer1)
print(lecturer2)
print(lecturer1.__add__(lecturer2))

