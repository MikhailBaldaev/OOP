class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, feedback):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.feedback_from_students:
                lecturer.feedback_from_students[course] += [feedback]
            else:
                lecturer.feedback_from_students[course] = [feedback]
        else:
            return('Ошибка')

    def __str__(self):
        self.courses_in_progress = ', '.join(self.courses_in_progress)
        self.finished_courses = ', '.join(self.finished_courses)
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_hw_grade()} \nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {self.finished_courses}'
        return text

    def average_hw_grade(self):
        total = 0
        quantity = 0
        for key, value in self.grades.items():
            for grade in value:
                total += grade
                quantity += 1
        average = round(total / quantity, 2)
        return average

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_hw_grade() == other.average_hw_grade()
        else:
            return('Ошибка')

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_hw_grade() != other.average_hw_grade()
        else:
            return('Ошибка')

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_hw_grade() >= other.average_hw_grade()
        else:
            return('Ошибка')

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_hw_grade() <= other.average_hw_grade()
        else:
            return('Ошибка')

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_hw_grade() > other.average_hw_grade()
        else:
            return('Ошибка')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_hw_grade() < other.average_hw_grade()
        else:
            return('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.feedback_from_students = {}

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_feedback()}'
        return text

    def average_feedback(self):
        total = 0
        quantity = 0
        for key, value in self.feedback_from_students.items():
            for feedback_value in value:
                total += feedback_value
                quantity += 1
        average = round(total / quantity, 2)
        return average

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_feedback() == other.average_feedback()
        else:
            return('Ошибка')

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_feedback() != other.average_feedback()
        else:
            return('Ошибка')

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_feedback() >= other.average_feedback()
        else:
            return('Ошибка')

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_feedback() <= other.average_feedback()
        else:
            return('Ошибка')

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_feedback() > other.average_feedback()
        else:
            return('Ошибка')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_feedback() < other.average_feedback()
        else:
            return('Ошибка')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return('Ошибка')

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text


cool_mentor = Reviewer('Some', 'Buddy')
cool_lect = Lecturer('Fir', 'Lect')
coolest_lect = Lecturer('Doc', 'Lector')
first_student = Student('John', 'Dow', 'male')
second_student = Student('Dale', 'Icewind', 'male')

first_student.courses_in_progress = ['Python', 'C++']
second_student.courses_in_progress = ['Python', 'C++']
cool_mentor.courses_attached += ['Python', 'C++']
cool_lect.courses_attached += ['Python', 'C++']
coolest_lect.courses_attached += ['Python', 'C++']

cool_mentor.rate_hw(first_student, 'Python', 4.4)
cool_mentor.rate_hw(first_student, 'Python', 5.5)
cool_mentor.rate_hw(first_student, 'Python', 6.6)
cool_mentor.rate_hw(first_student, 'C++', 2.2)
cool_mentor.rate_hw(first_student, 'C++', 2.1)
cool_mentor.rate_hw(second_student, 'Python', 6.6)
cool_mentor.rate_hw(second_student, 'C++', 6.6)

first_student.rate_lecturer(cool_lect, 'Python', 5.2)
second_student.rate_lecturer(cool_lect, 'Python', 6.2)
first_student.rate_lecturer(cool_lect, 'C++', 4.3)
first_student.rate_lecturer(coolest_lect, 'Python', 5.5)
second_student.rate_lecturer(coolest_lect, 'Python', 7.7)
first_student.rate_lecturer(coolest_lect, 'C++', 6.6)

list_students = [first_student, second_student]
list_lecturers = [coolest_lect, cool_lect]


def average_course_student(list, course):
    total = 0
    quantity = 0
    for student in list:
        for key, value in student.grades.items():
            if key == course:
                total += sum(value)
                quantity += len(value)
    average = round(total / quantity, 2)
    return f'Cредняя оценка за домашние задания в рамках курса {course} составляет {average}'


def average_course_lecturer(list, course):
    total = 0
    quantity = 0
    for lecturer in list:
        for key, value in lecturer.feedback_from_students.items():
            if key == course:
                total += sum(value)
                quantity += len(value)
    average = round(total / quantity, 2)
    return f'Cредняя оценка за лекции в рамках курса {course} составляет {average}'


print(average_course_lecturer(list_lecturers, 'Python'))
print(average_course_student(list_students, 'C++'))
