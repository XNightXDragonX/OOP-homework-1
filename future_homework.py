class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_l_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def counting_average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)
        if len(all_grades) > 0:
            average_grade = sum(all_grades) / len(all_grades)
        else:
            average_grade = 0
        return average_grade
        

    def __str__(self):
        average_grade = self.counting_average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n" 
                f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}\n")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        else:
            return self.counting_average_grade() == other.counting_average_grade()


def avarage_student_course_grade(students, course_name):
        total_grades = []
        for student in students:
            if course_name in student.grades:
                total_grades.extend(student.grades[course_name])
        if len(total_grades) > 0:
            return sum(total_grades) / len(total_grades)
        else:
            return 0


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def counting_average_grade_l(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)
        if len(all_grades) > 0:
            average_grade = sum(all_grades) / len(all_grades)
        else:
            average_grade = 0
        return average_grade

    def __str__(self):
        average_grade = self.counting_average_grade_l()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n" 
                f"Средняя оценка за лекции: {average_grade:.1f}\n")

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        else:
            return self.counting_average_grade_l() == other.counting_average_grade_l()


def average_lecturer_course_grade(lecturers, course_name):
        total_grades_l = []
        for lecturer in lecturers:
            if course_name in lecturer.grades:
                total_grades_l.extend(lecturer.grades[course_name])
        if len(total_grades_l) > 0:
            return sum(total_grades_l) / len(total_grades_l)
        else:
            return 0


class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


student_1 = Student('Sasaki', 'Haise', 'male')
student_2 = Student('Kaneki', 'Ken', 'male')

student_1.courses_in_progress += ['Literature']
student_1.courses_in_progress += ['PE']
student_2.courses_in_progress += ['Literature']
student_2.courses_in_progress += ['History']

student_1.finished_courses += ['Geometry']
student_1.finished_courses += ['Chemistry']
student_2.finished_courses += ['Geometry']
student_2.finished_courses += ['Biology']

lecturer_1 = Lecturer('Arima', 'Kishou')
lecturer_2 = Lecturer('Suzuya', 'Juuzou')

lecturer_1.courses_attached += ['Literature']
lecturer_2.courses_attached += ['Literature']
lecturer_1.courses_attached += ['PE']
lecturer_2.courses_attached += ['History']

reviewer_1 = Reviewer('Akira', 'Mado')
reviewer_2 = Reviewer('Amon', 'Koutarou')

reviewer_1.rate_hw(student_1, 'Literature', 8)
reviewer_1.rate_hw(student_2, 'PE', 10)
reviewer_2.rate_hw(student_1, 'Literature', 10)
reviewer_2.rate_hw(student_2, 'History', 10)

student_1.rate_l_hw(lecturer_1, 'Literature', 6)
student_1.rate_l_hw(lecturer_1, 'PE', 8)
student_1.rate_l_hw(lecturer_2, 'Literature', 10)
student_2.rate_l_hw(lecturer_1, 'Literature', 7)
student_2.rate_l_hw(lecturer_2, 'Literature', 9)
student_2.rate_l_hw(lecturer_2, 'History', 8)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

average_student_grade_res = avarage_student_course_grade(students, 'Literature')
average_lecturer_grade_res = average_lecturer_course_grade(lecturers, 'Literature')

print(f"Средняя оценка за домашние задания по курсу 'Literature': {average_student_grade_res}")
print(f"Средняя оценка за лекции по курсу 'Literature': {average_lecturer_grade_res:.1f}")











        
