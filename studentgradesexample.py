# Ogrenci isim, yas, not bilgisi olacak
# Ogrencinin derse kayit olmasini istiyoruz
# Dersin adi, max ogrenci sayisi tutulacak
# python dersine max 2 ogrenci kayit olabilsin
# Siz 3 ogrenci ekleyin
# Dersi alan ogrencilerin not ortalamasini bulunuz.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    

class Course:
    department = "compeng"
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Hilal", 29, 97)
s2 = Student("Ebrar", 20, 100)
s3 = Student("Sila", 22, 65)

c1 = Course("Python", 2)


print(c1.add_student(s1))
print(c1.add_student(s2))
print(c1.add_student(s3))

for student in c1.students:
    print(f"Student name: {student.name} age: {student.age} grade: {student.grade} ")

print(c1.get_average_grade())

c2 = Course("Math", 3)

Course.department = "machineeng"
print(c1.department)
print(c2.department)
print("*" * 30)
c2.department = "math"
print(c1.department)
print(c2.department)

print(Course.department)


