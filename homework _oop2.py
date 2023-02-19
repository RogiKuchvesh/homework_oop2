class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
       
    def mid_grade(self):
        self.all_grades = []
        for value in self.grades.values():
            self.all_grades.extend(value)
        return round(sum(self.all_grades) / len(self.all_grades), 2)

    def rate_lectors(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не наш студент')
            return
        else:
            return self.mid_grade() < other.mid_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mid_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.lec_grades = {}
        
    def mid_lec_grade(self):
        self.all_lec_grades = []
        for value in self.lec_grades.values():
            self.all_lec_grades.extend(value)
        return round(sum(self.all_lec_grades) / len(self.all_lec_grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не наш лектор')
            return
        else:
            return self.mid_lec_grade() < other.mid_lec_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_lec_grade()}'
        return res 

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

some_student = Student('Иван', 'Петров', 'муж')
same_student = Student('Ева', 'Иванова', 'жен')

student_list = [some_student, same_student]
def mid_grade_course(student_list, course):
    all_student_avg_grades = []
    for stu in student_list:
        if course in stu.courses_in_progress:            
            all_student_avg_grades.extend(stu.grades[course])
    return sum(all_student_avg_grades) / len(all_student_avg_grades)
 
some_student.courses_in_progress += ['Python', 'Введение в программирование']
same_student.courses_in_progress += ['Python', 'C++']
some_student.finished_courses += ['C++']
same_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Ivan', 'Palkin', ['Python', 'C++'])
same_lecturer = Lecturer('Irina', 'Kuchko', ['Python', 'Введение в программирование'])

lecturer_list = [some_lecturer, same_lecturer]
def mid_grade_lec_course(lecturer_list, course):
    all_lecturer_avg_grades = []
    for lec in lecturer_list:
        if course in lec.courses_attached:            
            all_lecturer_avg_grades.extend(lec.lec_grades[course])
    return sum(all_lecturer_avg_grades) / len(all_lecturer_avg_grades)

same_student.rate_lectors(some_lecturer, 'C++', 4)
same_student.rate_lectors(some_lecturer, 'Python', 10)
same_student.rate_lectors(same_lecturer, 'Python', 8)

some_student.rate_lectors(same_lecturer, 'Введение в программирование', 9)
some_student.rate_lectors(some_lecturer, 'Python', 10)
some_student.rate_lectors(same_lecturer, 'Python', 3)

print(some_lecturer.__lt__(same_lecturer))
print(some_lecturer.__str__())

print(same_lecturer.__lt__(some_lecturer))
print(same_lecturer.__str__())

# print(same_lecturer.lec_grades)
# print(some_lecturer.lec_grades)

some_reviewer = Reviewer('Serg', 'Orgony', ['Python', 'C++'])
same_reviewer = Reviewer('Nik', 'Pupkin', ['Python', 'Введение в программирование'])

print(some_reviewer.__str__())
print(same_reviewer.__str__())

some_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer.rate_hw(same_student, 'Python', 6)
some_reviewer.rate_hw(same_student, 'Python', 9)
some_reviewer.rate_hw(same_student, 'C++', 7)

same_reviewer.rate_hw(some_student, 'Python', 6)
same_reviewer.rate_hw(some_student, 'Python', 9)
same_reviewer.rate_hw(some_student, 'Введение в программирование', 9)
same_reviewer.rate_hw(same_student, 'Python', 6)
same_reviewer.rate_hw(same_student, 'Python', 9)
same_reviewer.rate_hw(same_student, 'Python', 7)

# print(some_student.grades)
# print(same_student.grades)

# print(some_student.mid_grade())
# print(same_student.mid_grade())

print(some_student.__lt__(same_student))
print(some_student.__str__())

print(same_student.__lt__(some_student))
print(same_student.__str__())

# print(some_lecturer.courses_attached)
# print(same_lecturer.courses_attached)

print(mid_grade_course([some_student, same_student], 'Python'))
print(mid_grade_lec_course([some_lecturer, same_lecturer], 'Python'))